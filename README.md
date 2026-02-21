# AI-Efficiency-Computation-Cost-Study-Using-Minesweeper
Minesweeper AI: Algorithmic Efficiency & Constraint-Based Inference
# Project Overview
This project is a comprehensive study of AI agent performance within the Minesweeper environment. The primary objective was to implement, benchmark, and optimize logic-based agents, focusing specifically on the computational trade-offs between simple deterministic logic and advanced subset inference.Key FeaturesThree-Tier Agent Architecture: Random Agent: Establishes a baseline for performance using stochastic moves.
Deterministic Agent: Employs basic logic to identify "safe" cells based on immediate neighbor counts.
Subset Inference Agent: Uses complex constraint-based reasoning to identify patterns that basic logic misses.
Modular Grid Engine: Designed with a decoupled architecture using separate visible and backend matrices for clean data handling.Automated Benchmarking: A built-in testing suite to evaluate agent success rates across varying difficulty levels.
# The Efficiency Study: Methodology & Complexity
The core of this research involved benchmarking agent performance across mine densities ranging from 1 to 30. Computational Trade-offsThe study analyzed the O(n^2) complexity of inference-based moves. While the Subset Inference Agent requires significantly higher computational cost per move compared to the Deterministic version, the research successfully justified this overhead by demonstrating a statistically significant increase in win rates, particularly in high-density environments.Shutterstock Explore Tech StackLanguage: Python Libraries: NumPy (for matrix manipulation), Matplotlib (for performance visualization) 
Tools: VS Code, Git/GitHub Results
Win-Rate Optimization: Demonstrated that subset reasoning provides the necessary edge to clear boards where local information is insufficient.
Performance Scaling: Identified the "tipping point" where increased density makes purely deterministic logic non-viable.
# About the Author
Htet Myat Aung BSc Computer Science (Artificial Intelligence) student at Royal Holloway, University of London.+1First Class Academic Average MENSA Member Specializing in Algorithmic Research and Logic-based AI
