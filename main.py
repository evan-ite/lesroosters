import libraries.helpers.load_data as ld
from libraries.algorithms.randomise import Random, random_algorithm
from libraries.classes.model import Model

if __name__ == "__main__":
    courses = ld.load_courses()
    students = ld.load_students(courses)
    halls = ld.load_halls()

    s = Model(courses, students, halls)
    r = Random(s.copy()).run()
    # print(s.get_highest_students(3))
    print(r.model)
    print(r.total_penalty())

    # start_time = time.time()

    print(r.total_penalty())

    # _________________________RANDOM ALGORITHM_______________________
    iterations = 1
    solution   = random_algorithm(iterations, s)

    print('THE BEST SCHEDULE FOUND WHEN USING RANDOM:\n', solution.model, '\n POINTS: ', solution.total_penalty())
    # ________________________________________________________________

    # with open("baseline.txt", "a+") as file:
    #     for _i in range(100000):
    #         random_schedule = Random(schedule, courses)
    #         random_schedule = random_schedule.run()
    #         penalty = Penalty(random_schedule)
    #         file.write(f"{penalty.total()}\n")

    # total_runtime = time.time() - start_time

    # print(time.strftime("%H:%M:%S", time.gmtime(total_runtime)))