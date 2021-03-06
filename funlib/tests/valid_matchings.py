def simple_chain():
    """
    target graph:

    A---->B---->C

    overcomplete graph:

    a--b--c--d--e
    """
    target_nodes = ["A", "B", "C"]
    target_edges = [("A", "B"), ("B", "C")]

    overcomplete_nodes = ["a", "b", "c", "d", "e"]
    overcomplete_edges = [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e")]

    node_costs = [
        ("a", "A", 1),
        ("b", "A", 5),
        ("b", "B", 5),
        ("c", "B", 1),
        ("d", "B", 5),
        ("d", "C", 5),
        ("e", "C", 1),
        ("a", None, 0),
        ("b", None, 0),
        ("c", None, 0),
        ("d", None, 0),
        ("e", None, 0),
    ]

    edge_costs = [
        (("a", "b"), ("A", "B"), 1),
        (("b", "c"), ("A", "B"), 1),
        (("b", "c"), ("B", "C"), 5),
        (("c", "d"), ("A", "B"), 5),
        (("c", "d"), ("B", "C"), 1),
        (("d", "e"), ("B", "C"), 1),
    ]

    expected_node_matchings = [
        ("a", "A"),
        ("b", None),
        ("c", "B"),
        ("d", None),
        ("e", "C"),
    ]

    expected_edge_matchings = [
        (("a", "b"), ("A", "B")),
        (("b", "c"), ("A", "B")),
        (("c", "d"), ("B", "C")),
        (("d", "e"), ("B", "C")),
    ]

    expected_cost = 7

    return (
        target_nodes,
        target_edges,
        overcomplete_nodes,
        overcomplete_edges,
        node_costs,
        edge_costs,
        expected_node_matchings,
        expected_edge_matchings,
        expected_cost,
    )


def short_chain():
    """
    target graph:

    A---->B---->C

    overcomplete graph:

        a--b--c
    """
    target_nodes = ["A", "B", "C"]
    target_edges = [("A", "B"), ("B", "C")]

    overcomplete_nodes = ["a", "b", "c"]
    overcomplete_edges = [("a", "b"), ("b", "c")]

    node_costs = [
        ("a", "A", 5),
        ("a", "B", 5),
        ("b", "B", 1),
        ("c", "B", 5),
        ("c", "C", 5),
        ("a", None, 0),
        ("b", None, 0),
        ("c", None, 0),
    ]

    edge_costs = [
        (("a", "b"), ("A", "B"), 1),
        (("a", "b"), ("B", "C"), 5),
        (("b", "c"), ("A", "B"), 5),
        (("b", "c"), ("B", "C"), 1),
    ]

    expected_node_matchings = [
        ("a", "A"),
        ("b", "B"),
        ("c", "C"),
    ]

    expected_edge_matchings = [
        (("a", "b"), ("A", "B")),
        (("b", "c"), ("B", "C")),
    ]

    expected_cost = 13

    return (
        target_nodes,
        target_edges,
        overcomplete_nodes,
        overcomplete_edges,
        node_costs,
        edge_costs,
        expected_node_matchings,
        expected_edge_matchings,
        expected_cost,
    )


def long_chain():
    """
    target graph:

        A---->B---->C

    overcomplete graph:

    a--b--c--d--e--f--g

    matching should not have too many edge assignments.
    """

    target_nodes = ["A", "B", "C"]
    target_edges = [("A", "B"), ("B", "C")]

    overcomplete_nodes = ["a", "b", "c", "d", "e", "f", "g"]
    overcomplete_edges = [
        ("a", "b"),
        ("b", "c"),
        ("c", "d"),
        ("d", "e"),
        ("e", "f"),
        ("f", "g"),
    ]

    node_costs = [
        ("a", "A", 5),
        ("b", "A", 1),
        ("c", "A", 5),
        ("c", "B", 5),
        ("d", "B", 1),
        ("e", "B", 5),
        ("e", "C", 5),
        ("f", "C", 1),
        ("g", "C", 5),
        ("a", None, 0),
        ("b", None, 0),
        ("c", None, 0),
        ("d", None, 0),
        ("e", None, 0),
        ("f", None, 0),
        ("g", None, 0),
    ]

    edge_costs = [
        (("a", "b"), ("A", "B"), 5),
        (("b", "c"), ("A", "B"), 1),
        (("c", "d"), ("A", "B"), 1),
        (("c", "d"), ("B", "C"), 5),
        (("d", "e"), ("A", "B"), 5),
        (("d", "e"), ("B", "C"), 1),
        (("e", "f"), ("B", "C"), 1),
        (("f", "g"), ("B", "C"), 5),
    ]

    expected_node_matchings = [
        ("a", None),
        ("b", "A"),
        ("c", None),
        ("d", "B"),
        ("e", None),
        ("f", "C"),
        ("g", None),
    ]

    expected_edge_matchings = [
        (("a", "b"), None),
        (("b", "c"), ("A", "B")),
        (("c", "d"), ("A", "B")),
        (("d", "e"), ("B", "C")),
        (("e", "f"), ("B", "C")),
        (("f", "g"), None),
    ]

    expected_cost = 7

    return (
        target_nodes,
        target_edges,
        overcomplete_nodes,
        overcomplete_edges,
        node_costs,
        edge_costs,
        expected_node_matchings,
        expected_edge_matchings,
        expected_cost,
    )


def simple_4_branch():
    """
    target graph:

          A
          |
          v
    B<----X---->C
          |
          v
          D

    overcomplete graph:

          a
          |
          b
          |
    c--d--e--f--g
          |
          h
          |
          i

    Matching should be able to match realistic 4 way junction
    """
    target_nodes = ["D", "B", "X", "A", "C"]
    target_edges = [("A", "X"), ("X", "B"), ("X", "C"), ("X", "D")]

    overcomplete_nodes = ["c", "d", "g", "f", "e", "b", "a", "h", "i"]
    overcomplete_edges = [
        ("a", "b"),
        ("b", "e"),
        ("e", "d"),
        ("d", "c"),
        ("e", "f"),
        ("f", "g"),
        ("e", "h"),
        ("h", "i"),
    ]

    node_costs = [
        ("a", "A", 1),
        ("b", "A", 5),
        ("b", "X", 5),
        ("c", "B", 1),
        ("d", "B", 5),
        ("d", "X", 5),
        ("e", "X", 1),
        ("f", "X", 5),
        ("f", "C", 5),
        ("g", "C", 1),
        ("h", "X", 5),
        ("h", "D", 5),
        ("i", "D", 1),
        ("a", None, 0),
        ("b", None, 0),
        ("c", None, 0),
        ("d", None, 0),
        ("e", None, 0),
        ("f", None, 0),
        ("g", None, 0),
        ("h", None, 0),
        ("i", None, 0),
    ]

    edge_costs = [
        (("a", "b"), ("A", "X"), 1),
        (("b", "e"), ("A", "X"), 1),
        (("b", "e"), ("X", "B"), 5),
        (("b", "e"), ("X", "C"), 5),
        (("b", "e"), ("X", "D"), 5),
        (("e", "d"), ("A", "X"), 5),
        (("e", "d"), ("X", "B"), 1),
        (("e", "d"), ("X", "C"), 5),
        (("e", "d"), ("X", "D"), 5),
        (("d", "c"), ("X", "B"), 1),
        (("e", "f"), ("A", "X"), 5),
        (("e", "f"), ("X", "B"), 5),
        (("e", "f"), ("X", "C"), 1),
        (("e", "f"), ("X", "D"), 5),
        (("f", "g"), ("X", "C"), 1),
        (("e", "h"), ("A", "X"), 5),
        (("e", "h"), ("X", "B"), 5),
        (("e", "h"), ("X", "C"), 5),
        (("e", "h"), ("X", "D"), 1),
        (("h", "i"), ("X", "D"), 1),
    ]

    expected_node_matchings = [
        ("e", "X"),
        ("a", "A"),
        ("b", None),
        ("c", "B"),
        ("d", None),
        ("g", "C"),
        ("f", None),
        ("i", "D"),
        ("h", None),
    ]

    expected_edge_matchings = [
        (("a", "b"), ("A", "X")),
        (("b", "e"), ("A", "X")),
        (("e", "d"), ("X", "B")),
        (("d", "c"), ("X", "B")),
        (("e", "f"), ("X", "C")),
        (("f", "g"), ("X", "C")),
        (("e", "h"), ("X", "D")),
        (("h", "i"), ("X", "D")),
    ]

    expected_cost = 13

    return (
        target_nodes,
        target_edges,
        overcomplete_nodes,
        overcomplete_edges,
        node_costs,
        edge_costs,
        expected_node_matchings,
        expected_edge_matchings,
        expected_cost,
    )


def confounding_chain():
    """
    target graph:

    A---->B---->C

    overcomplete graph:

     a--b--c--d--e
           |
           f--g--h

    the optimal matching should not assign anything to extra chain
    as long as using it is more expensive than c--d--e
    """

    target_nodes = ["A", "B", "C"]
    target_edges = [("A", "B"), ("B", "C")]

    overcomplete_nodes = ["a", "b", "c", "d", "e", "f", "g", "h"]
    overcomplete_edges = [
        ("a", "b"),
        ("b", "c"),
        ("c", "d"),
        ("d", "e"),
        ("c", "f"),
        ("f", "g"),
        ("g", "h"),
    ]

    node_costs = [
        ("a", "A", 1),
        ("b", "A", 5),
        ("b", "B", 5),
        ("c", "B", 1),
        ("d", "B", 5),
        ("d", "C", 5),
        ("e", "C", 1),
        ("f", "B", 3),
        ("g", "B", 6),
        ("g", "C", 6),
        ("h", "C", 3),
        ("a", None, 0),
        ("b", None, 0),
        ("c", None, 0),
        ("d", None, 0),
        ("e", None, 0),
        ("f", None, 0),
        ("g", None, 0),
        ("h", None, 0),
    ]

    edge_costs = [
        (("a", "b"), ("A", "B"), 1),
        (("b", "c"), ("A", "B"), 1),
        (("b", "c"), ("B", "C"), 5),
        (("c", "d"), ("A", "B"), 5),
        (("c", "d"), ("B", "C"), 1),
        (("d", "e"), ("B", "C"), 1),
        (("c", "f"), ("A", "B"), 5),
        (("c", "f"), ("B", "C"), 5),
        (("f", "g"), ("B", "C"), 3),
        (("g", "h"), ("B", "C"), 3),
    ]

    expected_node_matchings = [
        ("a", "A"),
        ("b", None),
        ("c", "B"),
        ("d", None),
        ("e", "C"),
        ("f", None),
        ("g", None),
        ("h", None),
    ]

    expected_edge_matchings = [
        (("a", "b"), ("A", "B")),
        (("b", "c"), ("A", "B")),
        (("c", "d"), ("B", "C")),
        (("d", "e"), ("B", "C")),
        (("c", "f"), None),
        (("f", "g"), None),
        (("g", "h"), None),
    ]

    expected_cost = 7

    return (
        target_nodes,
        target_edges,
        overcomplete_nodes,
        overcomplete_edges,
        node_costs,
        edge_costs,
        expected_node_matchings,
        expected_edge_matchings,
        expected_cost,
    )


def confounding_loop():
    """
    target graph:

    A---->B---->C


    overcomplete graph:

        a--b--c--d--e

            f--g
            | /
            h

    the optimal matching should not match all edges in a loop
    to the same edge to create an "infinite chain".
    """

    target_nodes = ["A", "B", "C"]
    target_edges = [("A", "B"), ("B", "C")]

    overcomplete_nodes = ["a", "b", "c", "d", "e", "f", "g", "h"]
    overcomplete_edges = [
        ("a", "b"),
        ("b", "c"),
        ("c", "d"),
        ("d", "e"),
        ("f", "g"),
        ("g", "h"),
        ("h", "f"),
    ]

    node_costs = [
        ("a", "A", 1),
        ("b", "A", 5),
        ("b", "B", 5),
        ("c", "B", 1),
        ("d", "B", 5),
        ("d", "C", 5),
        ("e", "C", 1),
        ("f", "B", 2),
        ("g", "B", 6),
        ("g", "C", 6),
        ("h", "B", 6),
        ("a", None, 0),
        ("b", None, 0),
        ("c", None, 0),
        ("d", None, 0),
        ("e", None, 0),
        ("f", None, 0),
        ("g", None, 0),
        ("h", None, 0),
    ]

    edge_costs = [
        (("a", "b"), ("A", "B"), 1),
        (("b", "c"), ("A", "B"), 1),
        (("b", "c"), ("B", "C"), 5),
        (("c", "d"), ("A", "B"), 5),
        (("c", "d"), ("B", "C"), 1),
        (("d", "e"), ("B", "C"), 1),
        (("f", "g"), ("B", "C"), 3),
        (("g", "h"), ("B", "C"), 3),
        (("h", "f"), ("B", "C"), 3),
    ]

    expected_node_matchings = [
        ("a", "A"),
        ("b", None),
        ("c", "B"),
        ("d", None),
        ("e", "C"),
        ("f", None),
        ("g", None),
        ("h", None),
    ]

    expected_edge_matchings = [
        (("a", "b"), ("A", "B")),
        (("b", "c"), ("A", "B")),
        (("c", "d"), ("B", "C")),
        (("d", "e"), ("B", "C")),
        (("h", "f"), None),
        (("f", "g"), None),
        (("g", "h"), None),
    ]

    expected_cost = 7

    return (
        target_nodes,
        target_edges,
        overcomplete_nodes,
        overcomplete_edges,
        node_costs,
        edge_costs,
        expected_node_matchings,
        expected_edge_matchings,
        expected_cost,
    )
