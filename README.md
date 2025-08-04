# Normalizing Flow Data Against Display

Due to the heterogenity intrinsic to our yeast display system, it is typical to see displaying cells that differ in total display signal by up to three orders of magnitude.

<img width="612" height="599" alt="A1 fcs_p1_p2_Single_Cells" src="https://github.com/user-attachments/assets/73fcf889-27b3-4710-9887-aa68e57b5ff3" />

Displaying cells have FITC intensities between 4*10^2 and 2*10^4

For this reason, any efforts to compare samples quantitatively must first normalize signal against the display level for the individual cell.

<img width="4263" height="4688" alt="Normalizing_Flow_Data_Against_Display" src="https://github.com/user-attachments/assets/45babadc-1e6e-4aea-9272-213abe9002e5" />


The code I’ve written loops through csv files. For each event, it takes the log10 of the specified flourophores and divides by the log10 of the display signal. It returns the summary statistics (mean, standard deviation, n) for each fluorophore for each file.

### Protocol

1. In FlowJo, gate on displaying cells
2. Export the populations to CSV files:
<img width="824" height="1244" alt="Screenshot_2025-08-04_at_10 28 24_AM" src="https://github.com/user-attachments/assets/7c75bd63-9fa5-46a9-b429-819c2a1b9dbd" />
<img width="1144" height="904" alt="Screenshot_2025-08-04_at_10 28 20_AM" src="https://github.com/user-attachments/assets/904dd483-25f5-4f65-8ae0-41b6d0ba91f2" />


3. Adjust the input directory and output filename
4. Adjust the names of the colors in the code
5. Run the code
