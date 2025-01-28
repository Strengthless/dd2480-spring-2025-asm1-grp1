# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots["MainTests::test_should_parse_correctly 1"] = (
    5,
    [
        {"x": 0.7833093523087367, "y": 0.9255692766915238},
        {"x": 0.8923463523464086, "y": 0.20103707721496367},
        {"x": 0.30150218035977105, "y": 0.5965171935630713},
        {"x": 0.41711243957602595, "y": 0.33328290615604916},
        {"x": 0.5621591436143982, "y": 0.8440773499582357},
    ],
    {
        "a_pts": 1,
        "area1": 1.0,
        "area2": 1.0,
        "b_pts": 1,
        "c_pts": 1,
        "d_pts": 1,
        "dist": 1.0,
        "e_pts": 1,
        "epsilon": 0.1,
        "f_pts": 1,
        "g_pts": 1,
        "k_pts": 1,
        "length1": 2.0,
        "length2": 1.0,
        "n_pts": 1,
        "q_pts": 1,
        "quads": 1,
        "radius1": 1.0,
        "radius2": 1.0,
    },
    [
        [
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
        ],
        [
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
        ],
        [
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
        ],
        [
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
        ],
        [
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
        ],
        [
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
        ],
        [
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
        ],
        [
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
        ],
        [
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
        ],
        [
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
        ],
        [
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
        ],
        [
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
        ],
        [
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
        ],
        [
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
        ],
        [
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
        ],
    ],
    [
        True,
        False,
        True,
        True,
        False,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        False,
        True,
        False,
    ],
)

snapshots[
    "MainTests::test_should_parse_correctly Correct inputs should be parsed correctly."
] = (
    5,
    [
        {"x": 0.7833093523087367, "y": 0.9255692766915238},
        {"x": 0.8923463523464086, "y": 0.20103707721496367},
        {"x": 0.30150218035977105, "y": 0.5965171935630713},
        {"x": 0.41711243957602595, "y": 0.33328290615604916},
        {"x": 0.5621591436143982, "y": 0.8440773499582357},
    ],
    {
        "a_pts": 1,
        "area1": 1.0,
        "area2": 1.0,
        "b_pts": 1,
        "c_pts": 1,
        "d_pts": 1,
        "dist": 1.0,
        "e_pts": 1,
        "epsilon": 0.1,
        "f_pts": 1,
        "g_pts": 1,
        "k_pts": 1,
        "length1": 2.0,
        "length2": 1.0,
        "n_pts": 1,
        "q_pts": 1,
        "quads": 1,
        "radius1": 1.0,
        "radius2": 1.0,
    },
    [
        [
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
        ],
        [
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
        ],
        [
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
        ],
        [
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
        ],
        [
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
        ],
        [
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
        ],
        [
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
        ],
        [
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
        ],
        [
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
        ],
        [
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
        ],
        [
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
        ],
        [
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
        ],
        [
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
        ],
        [
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
        ],
        [
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.ORR: 2>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.ANDD: 1>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
            GenericRepr("<Connectors.NOTUSED: 777>"),
        ],
    ],
    [
        True,
        False,
        True,
        True,
        False,
        False,
        True,
        False,
        True,
        False,
        True,
        False,
        False,
        True,
        False,
    ],
)
