import numpy as np
import pandas as pd

def calculate_normal_equation(filepath, round_digits=3):
    """
    Calculate the optimal parameters using the Normal Equation method.
    
    Parameters:
    filepath (str): Path to the Excel or CSV file containing the data
    round_digits (int): Number of digits to round the results to
    
    Returns:
    ndarray: Array of theta parameters
    """
    try:
        # Try to load as Excel file first
        try:
            data = pd.read_excel(filepath)
        except:
            # If not an Excel file, try CSV
            data = pd.read_csv(filepath)
        
        print(f"Successfully loaded data with {len(data)} rows and {len(data.columns)} columns")
        print(f"Column names: {data.columns.tolist()}")
        
        # Extract features (X) and target variable (y)
        # Assuming first columns are features and last column is target
        X = data.iloc[:, :-1].values
        y = data.iloc[:, -1].values
        
        # Add a column of 1's for the intercept term
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        
        # Calculate using the Normal Equation: θ = (X^T X)^(-1) X^T y
        # Step 1: Calculate X^T X
        XTX = X_b.T.dot(X_b)
        
        # Step 2: Calculate (X^T X)^(-1)
        XTX_inv = np.linalg.inv(XTX)
        
        # Step 3: Calculate (X^T X)^(-1) X^T
        XTX_inv_XT = XTX_inv.dot(X_b.T)
        
        # Step 4: Calculate θ = (X^T X)^(-1) X^T y
        theta = XTX_inv_XT.dot(y)
        
        # Round the results to the specified number of digits
        theta_rounded = np.round(theta, round_digits)
        
        # Print the results
        print("\nOptimal theta parameters:")
        for i, t in enumerate(theta_rounded):
            print(f"theta{i} = {t}")
        
        return theta_rounded
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# If running the script directly
if __name__ == "__main__":
    import sys
    
    # Check if a filename was provided as a command-line argument
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        calculate_normal_equation(filepath)
    else:
        # Example usage with prompt for the file path
        filepath = input("Enter the path to your Excel or CSV file: ")
        calculate_normal_equation(filepath)