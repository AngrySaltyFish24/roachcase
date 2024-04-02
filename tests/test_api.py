import pytest
import roachcase


def test_set_persistence():
    observed = roachcase.list_players()
    assert observed == []
    roachcase.add_player("Bob")
    observed = roachcase.list_players()
    assert observed == ["Bob"]
    # this resets persistence
    roachcase.set_persistence("memory")
    observed = roachcase.list_players()
    assert observed == []


@pytest.fixture
def mem_persistance():
    roachcase.set_persistence("memory")
    yield
    roachcase.set_persistence("memory")


class TestPlayerManagement:
    def check_empty_list_players(self):
        observed = roachcase.list_players()
        assert observed == []

    def check_add_players(self):
        roachcase.add_player("Bob")
        roachcase.add_player("Alice")
        observed = roachcase.list_players()
        assert set(observed) == set(["Alice", "Bob"])

    def check_remove_players(self):
        roachcase.remove_player("Alice")
        observed = roachcase.list_players()
        assert set(observed) == set(["Bob"])

    @pytest.mark.usefixtures("mem_persistance")
    def test_management(self):
        self.check_empty_list_players()
        self.check_add_players()
        self.check_remove_players()
