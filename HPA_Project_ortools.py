from ortools.sat.python import cp_model
import sys

def read_input(input_path):
    with open(input_path, 'r') as file:
        num_cities = int(file.readline().strip())
        num_edges = int(file.readline().strip())
        adj = [[] for _ in range(num_cities)]
        for _ in range(num_edges):
            p = file.readline().split()
            if len(p) == 2:
                adj[int(p[1])].append(int(p[0]))
                adj[int(p[0])].append(int(p[1]))
    return num_cities, adj 

def write_output(output_path, solution):
    with open(output_path, 'w') as f:
        f.write(solution + '\n')

def solve_power_plant_problem(num_cities, adj):
    solution = [1 for _ in range(num_cities)]
    # Create the CP-SAT model
    model = cp_model.CpModel()
    
    # Create variables: 1 if a power plant is placed in city i, 0 otherwise
    power_plants = [model.NewBoolVar(f'power_plant_{i}') for i in range(num_cities)]
    model.Minimize(sum(power_plants))
    
    # Add constraints: Each city must be covered either by its own power plant
    # or by a power plant in an adjacent city
    for i in range(num_cities):
        line = adj[i]
        model.Add(sum(power_plants[i] + power_plants[n] for n in line) >= 1)
    
    # Objective: Minimize the total number of power plants
    model.Minimize(sum(power_plants))
    
    # Solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    
    if status == cp_model.OPTIMAL:
        # Get the solution as a binary string
        solution = ''.join('1' if solver.Value(power_plants[i]) else '0' for i in range(num_cities))
        return solution
    else:
        return "No solution found"

# Main program
def main():
    if len(sys.argv) != 3:
        print("Usage: python HPA_Project.py <input_file> <output_file>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    # Solve the problem
    num_cities, adj = read_input(input_path)
    solution = solve_power_plant_problem(num_cities, adj)
    write_output(output_path, solution)
    
    return solution

if __name__ == "__main__":
    main()