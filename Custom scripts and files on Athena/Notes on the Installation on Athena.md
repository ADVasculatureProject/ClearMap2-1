

# Notes about the installation process of TubeMap

Last updated: 7th June 2020, Peter Rupprecht


## Installation of dependencies:

- Using C. Kirst's yml-file
- Delete "torch" from the package list in the yml-file, it is not needed and creates arrors
- Downgrade numpy because of pickle file issues (conda install -c conda-forge numpy=1.16.2)
- p3d-plot did not work (specifically on Athena, unclear why). Solution: conda install -c conda-forge pyqtgraph=0.10.0; previously, version 0.11.0... was installed.

## Bugs and issues in TubeMap

- If the file '/home/athena-admin/Desktop/git_env/ClearMap2/ClearMap/ImageProcessing/Binary/Smoothing.npy' is missing, it will be computed again from scratch, which will take ca. 24 hours.
- Binarization of arteries: error when loading vasc.default parameters. Solved by writing "processing_parameter = vasc.default_binarization_processing_parameter.copy()". Hopefully this is correct :-)
- Vessel filling stopped with error due to mismatching dimensions of torch arrays. Problem in the line
"result = torch.max(torch.max(result[result_slicing], data[data_slicing]), sink_prev)" in the VesselFilling.py script.
Solution: Inserting into VesseFilling.py before this point: "result_slicing = (0,) +(0,) + result_slicing"

## Data structures and principles of TubeMap

- "ws" (for "workspace") is a variable that describes the currently used dataset (filenames, etc.)
- ws.info() gives some information about the current state
- ws.debug = True; and ws.debug = False; switch between two modes. If the workspace is in the wrong mode, files will not be detected (wrong filenames). A typical error then is "cannot create memmap without shape!" or something similar.
- all output files are saved to the main folder ('directory'). These are either small (layout file for stitching), or they are large (entire stitched dataset as npy-file, easily severall 100 GiB)


# Notes about the installation process of TubeMap on Demeter

Last updated: 28th September 2020, Peter Rupprecht

- Problem with the dataviewer, crashes when trying to plot something
- Is due to .../ClearMap/Visualization/Qt/DataViewer.py, line with "splitter.addWidget(lut_widget)"
- Commenting this line removes the LUTs but prevents the crash

October 6th:

- Problem with plotting binary npy stacks. Solved by uncommenting lines following l. 460 ("# avoid bools") in "DataViewer.py".
