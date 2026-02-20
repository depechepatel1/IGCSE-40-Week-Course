import cProfile
import pstats
from generate_course import generate_html_files

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    generate_html_files()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats(20)
