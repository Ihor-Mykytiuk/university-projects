package lab2;

import java.util.ArrayList;

public class House {
    private ArrayList<Room> rooms;

    House () {
        rooms = new ArrayList<>();
    }

    public ArrayList<Room> getHouse() {
        return rooms;
    }

    public void setHouse(ArrayList<Room> rooms) {
        this.rooms = rooms;
    }

    public void addRoom(Room room) {
        rooms.add(room);
    }
}
