#!/usr/bin/env python3
"""A module which contains function defining `index_range`"""


def index_range(page, page_size):
    """Returning a tuple of size two containing a start index and an end index"""
    start_idx = page_size * (page - 1)
    end_idx = page_size * page

    return (start_idx, end_idx)
