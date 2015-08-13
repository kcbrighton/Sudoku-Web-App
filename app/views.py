from flask import render_template, request, redirect, url_for, send_from_directory
from flask import flash
from app import app
from werkzeug import secure_filename
import os
import numpy as np

from SudokuImage import SudokuImage
from Sudoku import Sudoku

#from extract_sudoku_data import extract_cells, solve_sudoku, find_empty_cell
#from extract_sudoku_data import *

# ROUTING/VIEW FUNCTIONS

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the name of the uploaded file
        file = request.files['file']
        
        if file and allowed_file(file.filename):
            
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return redirect(url_for('sudoku',
                                    fname = filename))

    return render_template('index.html')




@app.route('/image/<fname>', methods = ['GET', 'POST'])
def sudoku(fname):

    f_path = os.path.join(app.config['UPLOAD_FOLDER'], fname)
    
    sdku_img = SudokuImage(f_path)     # create sudokuimage object

    sudoku_grid = np.zeros((9,9), dtype = int)
    # note: empty cells will be denoted by 0        
    

    # use knn to predict the value of non-empty sdku_img cells
    for cell in sdku_img.predict_cells():
        sudoku_grid[cell[0], cell[1]] = cell[2]

    no_failure = True
    solved_grid = sudoku_grid.copy()

    if request.method == 'POST':
        sdku = Sudoku(solved_grid) # create sudoku object
        no_failure, solution = sdku.solve() # solve sudoku
        
        

    if no_failure:
        return render_template('sudoku_image.html',image =
                               url_for('static', 
                                       filename = 'uploaded_sudokus/'+fname),
                               initial_sudoku = sudoku_grid, 
                               solved_sudoku = solved_grid)
    else:
        flash("Oops, I am having trouble with your Sudoku!  Let's try this again.")
        return redirect(url_for('sudokusolver'))


@app.route('/sudokusolver',methods=['GET', 'POST'])
def sudokusolver():

    if request.method == 'POST':
        # Get the name of the uploaded file
        file = request.files['file']
        
        if file and allowed_file(file.filename):
            
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            return redirect(url_for('sudoku',
                                    fname = filename))

    return render_template('sudokusolver.html')
