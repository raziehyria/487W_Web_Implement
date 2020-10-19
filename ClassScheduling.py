from config import Config
from display.display import DisplayMgr
from geneticalgorithm import GeneticAlgorithm
from population import Population

#  added the try-catch block because I was getting exception error from the Config class
try:
    config = Config()
except Exception:
    config = Config.getInstance()

display_manager = DisplayMgr()

population = Population(config.get_POPULATION_SIZE())
genAlgo = GeneticAlgorithm(config)

population.sort_schedules()
#print(population)

generationCount = 0
no_change_count = 0
prev_fitness = 0
while no_change_count < config.get_MAX_ITERATION():
    best_schedule = population.get_schedules()[0]

    # display_manager.print_conflicts((best_schedule))

    best_schedule_fitness = best_schedule.get_fitness()
    if best_schedule_fitness >= 0.5:
        break
    population = genAlgo.evolve(population)
    generationCount += 1
    if prev_fitness == best_schedule_fitness:
        no_change_count += 1
    else:
        no_change_count = 0
        prev_fitness = best_schedule_fitness
    print("Generation #: {} - #MajorConflict: {} - #MinorConflict: {} - Fitness: {} - No Change Count {}".format(generationCount,
                                                                                       best_schedule.get_numberofMajorConflicts(),
                                                                                       best_schedule.get_numberofMinorConflicts(),
                                                                                       best_schedule_fitness,
                                                                                       no_change_count))
display_manager.print_schedule(best_schedule)
