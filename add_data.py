from db import get_session, TeamStatistic
from sqlalchemy.orm.exc import NoResultFound

def add_data_to_db(wins_all, wins_home, wins_guests, wins_in_a_row,
                   loses_all, loses_home, loses_guests, loses_in_a_row):

    session = get_session()  
    
    try:
        new_team = TeamStatistic(
            wins_all=wins_all,
            wins_home=wins_home,
            wins_guests=wins_guests,
            wins_in_a_row=wins_in_a_row,
            loses_all=loses_all,
            loses_home=loses_home,
            loses_guests=loses_guests,
            loses_in_a_row=loses_in_a_row
        )
        session.add(new_team)
        session.commit()
        print("Data added successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()

    finally:
        session.close()  # Закрываем сессию, созданную внутри функции
