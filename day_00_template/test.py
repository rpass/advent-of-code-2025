import subprocess
import os
import sys


def run_solution():
    """Run solution.py and capture its output."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    solution_path = os.path.join(script_dir, "solution.py")
    
    result = subprocess.run(
        [sys.executable, solution_path],
        capture_output=True,
        text=True,
        cwd=script_dir
    )
    
    return result.stdout.strip(), result.stderr, result.returncode


def test_solution():
    """Test the solution against expected output."""
    # Define expected output here
    expected_output = ""  # TODO: Set your expected output here
    
    # Run the solution
    actual_output, stderr, return_code = run_solution()
    
    # Check if the solution ran successfully
    if return_code != 0:
        print(f"❌ Solution failed with return code {return_code}")
        if stderr:
            print(f"Error: {stderr}")
        return False
    
    # Compare outputs
    if actual_output == expected_output:
        print("✅ Test passed! Output matches expected result.")
        print(f"Output: {actual_output}")
        return True
    else:
        print("❌ Test failed! Output does not match expected result.")
        print(f"Expected: {repr(expected_output)}")
        print(f"Actual:   {repr(actual_output)}")
        return False


if __name__ == "__main__":
    success = test_solution()
    sys.exit(0 if success else 1)

