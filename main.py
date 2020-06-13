from design_pattern_miner.matching import DesignPatternMatcher
from design_pattern_miner.design_patterns import design_patterns
from design_pattern_miner.func import read_graph

if __name__ == "__main__":
    g = read_graph("planning.edges.csv")
    dpm = DesignPatternMatcher(g, design_patterns)
    print(dpm.match_all())
    print(dpm.get_quality_value())