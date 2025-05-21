class SparseMatrix:
    def __init__(self, filepath=None, rows=0, cols=0):
        # Initialize the matrix with number of rows and columns
        # Or load it from a file if a filepath is given
        self.rows = rows
        self.cols = cols
        self.data = {}  # Dictionary to hold non-zero values: (row, col) => value

        if filepath:
            self.load_from_file(filepath)

    def load_from_file(self, filepath):
        # This function reads the matrix from a file
        try:
            with open(filepath, 'r') as file:
                lines = []

                # Read all non-empty lines
                for line in file:
                    line = line.strip()
                    if line != "":
                        lines.append(line)

                # Check if the first two lines are valid
                if not lines[0].startswith("rows=") or not lines[1].startswith("cols="):
                    raise ValueError("Input file has wrong format")

                # Get number of rows and columns
                self.rows = int(lines[0].split('=')[1])
                self.cols = int(lines[1].split('=')[1])

                # Read matrix values from the file
                for line in lines[2:]:
                    if not (line.startswith("(") and line.endswith(")")):
                        raise ValueError("Input file has wrong format")

                    # Remove the brackets and split the values
                    parts = line[1:-1].split(',')
                    if len(parts) != 3:
                        raise ValueError("Input file has wrong format")

                    # Convert values to integers
                    row = int(parts[0].strip())
                    col = int(parts[1].strip())
                    val = int(parts[2].strip())

                    # Only store non-zero values
                    if val != 0:
                        self.set_element(row, col, val)

        except Exception:
            raise ValueError("Input file has wrong format")

    def get_element(self, row, col):
        # Return the value at (row, col) or 0 if not found
        return self.data.get((row, col), 0)

    def set_element(self, row, col, value):
        # Set the value at (row, col)
        # If value is 0, remove it from storage
        if value != 0:
            self.data[(row, col)] = value
        else:
            if (row, col) in self.data:
                del self.data[(row, col)]

    def add(self, other):
        # Add two matrices together
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix sizes must be the same for addition")

        result = SparseMatrix(rows=self.rows, cols=self.cols)

        # Add all values from both matrices
        all_positions = set(self.data.keys()).union(other.data.keys())
        for pos in all_positions:
            sum_val = self.get_element(*pos) + other.get_element(*pos)
            result.set_element(pos[0], pos[1], sum_val)

        return result

    def subtract(self, other):
        # Subtract another matrix from this one
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix sizes must be the same for subtraction")

        result = SparseMatrix(rows=self.rows, cols=self.cols)

        # Subtract all values from both matrices
        all_positions = set(self.data.keys()).union(other.data.keys())
        for pos in all_positions:
            diff_val = self.get_element(*pos) - other.get_element(*pos)
            result.set_element(pos[0], pos[1], diff_val)

        return result

    def multiply(self, other):
        # Multiply two matrices
        if self.cols != other.rows:
            raise ValueError("Number of columns of first matrix must equal number of rows of second")

        result = SparseMatrix(rows=self.rows, cols=other.cols)

        for (r1, c1), v1 in self.data.items():
            for c2 in range(other.cols):
                v2 = other.get_element(c1, c2)
                if v2 != 0:
                    old_val = result.get_element(r1, c2)
                    result.set_element(r1, c2, old_val + v1 * v2)

        return result

    def __str__(self):
        # Return a readable version of the matrix
        result = f"rows={self.rows}\ncols={self.cols}\n"
        for (row, col), value in self.data.items():
            result += f"({row}, {col}, {value})\n"
        return result.strip()
