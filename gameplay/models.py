from django.db import models
# Players of the game = users of the site
from django.contrib.auth.models import User

# Drop-down menu for django admin panel
GAME_STATUS_CHOICE = (

    ('F', 'First Player Move'),
    ('S', 'Second Player Move'),
    ('W', 'First Player Wins'),
    ('L', 'Second PLayer Wins'),
    ('D', 'Draw')

)


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    # blank = True is for leaving the comment field empty
    # This won't affect the CharField in DB as it will be
    # not null as it is by default
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()


class Game(models.Model):
    # First_player and Second player are fields
    # that will hold the user model.
    # Games_first_player will hold the collection of all the games
    # with the user as first player.
    first_player = models.ForeignKey(User,
                                     related_name="game_first_payer")
    second_player = models.ForeignKey(User,
                                      related_name="game_second_payer")

    # Timestamp
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='F',
                              choices=GAME_STATUS_CHOICE)

    def __str__(self):
        return "{0} vs {1}".format(
            self.first_player, self.second_player)
