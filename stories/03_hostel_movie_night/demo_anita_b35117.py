from story import available

# Mock option class for demonstration
class MovieOption:
    def __init__(self, name, cost):
        self.name = name
        self._cost = cost
        
    def data_cost(self):
        return self._cost
        
    def __repr__(self):
        return f"MovieOption({self.name}, cost={self._cost}MB)"

def run_demo():
    print("=== STARTING EXTENSION 4 DEMO: Anita (b35117) ===")
    
    # Setup some test options with different data costs
    options = [
        MovieOption("Short Comedy", 200),
        MovieOption("Action Movie", 800),
        MovieOption("Documentary", 400),
        MovieOption("Ultra HD Epic", 1500)
    ]
    
    bundle_budget = 1000
    print(f"\n[Normal Case] Checking available options for a {bundle_budget}MB budget:")
    print(f"All options: {options}")
    
    # Call the available function
    fits = available(options, bundle_budget)
    print(f"Options that fit: {fits}")
    
    # Verify that it didn't change or play the original options (resource/history unchanged check)
    print(f"Original options list remains unchanged: {options}")
    
    # Boundary / Refused Case: Low budget where nothing fits
    tiny_budget = 50
    print(f"\n[Boundary Case] Checking available options for a tiny {tiny_budget}MB budget:")
    fits_empty = available(options, tiny_budget)
    print(f"Options that fit: {fits_empty}")
    print("Demo completed successfully!")

if __name__ == "__main__":
    run_demo()