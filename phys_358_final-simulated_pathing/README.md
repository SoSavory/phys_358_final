# phys_358_final
Simulated Annealing


Logic:

The City is simulated by a graph which is made up of nodes, edges between the nodes, and a single traveler.

There is a global time for the simulation, which starts at 0.

Each edge has a "traversibility frequency" associated with it, which uses the global time to determine whether or not that edge is traversible.

The traveler exists at a node.

The traveler can make a move across any traversible edge connected to the node they are on.

Each edge has an associated time cost of traversal. This time cost is modeled by distance/speed limit, but could include other factors like a traffic congestion coefficient or similar.

The traveler uses some algorithm for deciding which move to make.

After that move, the time of the simulation updates, and therefore so do the traversibility property of all edges.


How to initialize the graph:
  for a super simple graph of
  a -> c
  need a graph dictionary that looks something like:

  graph = { "a" : [{node: "c", time_cost: 5, traversible: true, traversible_function: f(t)}],
            "c" : [{node: "a", time_cost: 5, traversible: false, traversible_function: g(t) }]
          }
