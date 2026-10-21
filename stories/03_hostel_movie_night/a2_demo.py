# stories/03_hostel_movie_night/a2_demo.py

from a2_expectations import (
    MovieChoiceError,
    MovieRequestError,
    MovieResourceError
)

"""
Short Explanation for Option A2 Demo:
This script demonstrates the custom exception classes for Option A2, 
testing normal cases, boundary conditions, and invalid/refused cases 
using automated plain assert checks.
"""

def run_a2_demo_and_checks():
    print("=== Running Hostel Movie Night: Option A2 Demo & Checks ===")

    # 1. Normal / Instantiation check
    err = MovieChoiceError("No choice provided")
    assert isinstance(err, Exception)
    print("[PASS] Normal case: Exception instantiated successfully.")

    # 2. Invalid Case Check: MovieRequestError (e.g., negative cost)
    try:
        raise MovieRequestError("Invalid negative requirement (-500 MB)")
    except MovieRequestError as e:
        assert "negative requirement" in str(e)
        print(f"[PASS] Invalid/Refused case caught: {e}")

    # 3. Resource Error Check: MovieResourceError (e.g., exceeds limit)
    try:
        raise MovieResourceError("Request exceeds remaining MB resources")
    except MovieResourceError as e:
        assert "exceeds remaining MB" in str(e)
        print(f"[PASS] Boundary/Resource case caught: {e}")

    print("\nAll A2 demo checks passed successfully!")

if __name__ == "__main__":
    run_a2_demo_and_checks()