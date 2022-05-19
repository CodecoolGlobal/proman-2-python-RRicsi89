import data_manager


def get_card_status(status_id):
    """
    Find the first status matching the given id
    :param status_id:
    :return: str
    """
    status = data_manager.execute_select(
        """
        SELECT * FROM statuses s
        WHERE s.id = %(status_id)s
        ;
        """
        , {"status_id": status_id})

    return status


def get_boards():
    """
    Gather all boards
    :return:
    """
    # remove this code once you implement the database
    # return [{"title": "board1", "id": 1}, {"title": "board2", "id": 2}]

    return data_manager.execute_select(
        """
        SELECT * FROM boards
        ORDER BY id
        ;
        """
    )


def get_cards_for_board(board_id):
    # remove this code once you implement the database
    # return [{"title": "title1", "id": 1}, {"title": "board2", "id": 2}]

    matching_cards = data_manager.execute_select(
        """
        SELECT * FROM cards
        WHERE cards.board_id = %(board_id)s
        ORDER BY status_id, card_order
        ;
        """
        , {"board_id": board_id})

    return matching_cards


def save_new_board(board_title):
    data_manager.execute_update(
    """
    INSERT INTO boards (title)
    VALUES (%(board_title)s);
    """, {"board_title": board_title})


def rename_board(board_id, board_title):
    title = data_manager.execute_update(
        """
        UPDATE boards
        SET title = %(board_title)s
        WHERE id = %(board_id)s
        ;
        """
        , {"board_title": board_title, "board_id": board_id})

    return title


def count_cards(board_id, status_id):
    result = data_manager.execute_select(
        """
        SELECT COUNT(id) FROM cards
        WHERE (board_id = %(board_id)s AND status_id = %(status_id)s)
        """, {"board_id": board_id, "status_id": status_id}
    )
    return result


def update_card_status(card_id, status_id, card_order):
    data_manager.execute_update(
        """
        UPDATE cards
        SET status_id = %(status_id)s, card_order = %(card_order)s
        WHERE id = %(card_id)s;
        """, {"card_id": card_id, "status_id": status_id, "card_order": card_order}
    )

def delete_card(card_id):
    data_manager.execute_update(
    """
        DELETE FROM cards
        WHERE id = %(card_id)s
    """, {"card_id": card_id}
    )