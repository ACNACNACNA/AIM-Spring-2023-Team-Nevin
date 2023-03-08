from EvolutionSimulator import EvolutionSimulator

sim = EvolutionSimulator()
print("Generation 0:")
sim.show_images()
for i in range(200):
    sim.evaluate_fitness()
    sim.kill_population()
    sim.reproduce()
print("Generation 200:")
sim.show_images()