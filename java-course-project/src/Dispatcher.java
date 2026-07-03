import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;


public class Dispatcher {
    public static void main(String[] args) {
        File inputFiles = new File("D:\\CourseProject\\inputFiles");
        File outputFiles = new File("D:\\CourseProject\\outputFiles");
        inputFiles.mkdirs();
        outputFiles.mkdirs();

        File f1 = new File(inputFiles, "footballers_data_file1.txt");
        File f2 = new File(inputFiles, "footballers_data_file2.txt");
        File f3 = new File(inputFiles, "footballers_data_file3.txt");

        Controller.handleFiles(outputFiles, f1, f2, f3);
        System.out.println("files read and wrote");

    }
}

class Footballer implements Comparable<Footballer> {
    private String name;
    private String country;
    private int age;

    public Footballer(String name, String country, int age) {
        this.name = name;
        this.country = country;
        this.age = age;
    }

    public String getName() {
        return this.name;
    }

    public String getCountry() {
        return this.country;
    }

    public int getAge() {
        return this.age;
    }

    @Override
    public String toString() {
        return "Footballer{" +
                "name='" + name + '\'' +
                ", country='" + country + '\'' +
                ", age=" + age +
                '}';
    }

    @Override
    public int compareTo(Footballer footballer) {
        int result = this.name.compareTo(footballer.name);
        if (result != 0) {
            return result;
        } else {
            result = this.country.compareTo(footballer.country);
            if (result != 0) {
                return result;
            } else {
                return Integer.compare(this.age, footballer.age);
            }
        }
    }
}

class Controller {
    public static final ArrayList<Footballer> YOUNG_AGE_FOOTBALLERS = new ArrayList<>();
    public static final ArrayList<Footballer> MIDDLE_AGED_FOOTBALLERS = new ArrayList<>();
    public static final ArrayList<Footballer> OLD_AGE_FOOTBALLERS = new ArrayList<>();

    public static void handleFiles(File outputFilesDir, File ... files) {
        String typeSort = inputSortType();

        for(File file : files) {
            try {
                readFile(file);
            } catch (FileNotFoundException fnfe) {
                System.out.println("file for read with path " + file.getPath() + " not exist!");
            } catch (IOException ioe) {
                System.out.println("error while reading file with path " + file.getPath());
            }
            sortFootballers(typeSort);
            writeFiles(outputFilesDir);
        }
    }

    private static String inputSortType() {
        System.out.println("select file sort type:\n1 - by name\n2 - by country\n3 - by age\nsomething else - default");
        Scanner input = new Scanner(System.in);
        String str = "";
        try {
            int type = input.nextInt();
            if(type == 1) {
                str = "name";
            } else if (type == 2) {
                str = "country";
            } else if (type == 3) {
                str = "age";
            }
        }
        catch (Exception e) {
            str = "default";
        }
        System.out.println("your choice is " + str + " sort");
        return str;
    }

    private static void readFile(File file) throws IOException{
        String line = "";
        BufferedReader br = new BufferedReader(new FileReader(file));
        while ((line = br.readLine()) != null){
            ArrayList<String> list = new ArrayList<>();
            splitLine(line, list);
            separateFootballer(new Footballer(list.get(1), list.get(2), Integer.parseInt(list.get(3))));
        }
        br.close();
    }

    private static void splitLine(String line, ArrayList<String> list) {
        String[] array = line.split(" ");
        for(String str : array) {
            if (!str.isEmpty()) {
                list.add(str);
            }
        }
    }

    private static void separateFootballer(Footballer footballer){
        int age = footballer.getAge();
        if (age < 22) {
            YOUNG_AGE_FOOTBALLERS.add(footballer);
        } else if (age >= 22 && age <= 27) {
            MIDDLE_AGED_FOOTBALLERS.add(footballer);
        } else {
            OLD_AGE_FOOTBALLERS.add(footballer);
        }
    }

    private static void writeFiles(File outputFilesDir) {
        File[] outputFiles = {new File(outputFilesDir, "youngAgeFootballers.txt"),
                new File(outputFilesDir, "middleAgedFootballers.txt"),
                new File(outputFilesDir, "oldAgeFootballers.txt")};
        try {
            PrintWriter pw = new PrintWriter(new File(outputFilesDir, "youngAgeFootballers.txt"));
            for(int i = 0; i < YOUNG_AGE_FOOTBALLERS.size(); i++) {
                pw.println("" + i + " " + YOUNG_AGE_FOOTBALLERS.get(i));
            }
            pw.flush();
            pw.close();

            pw = new PrintWriter(new File(outputFilesDir, "middleAgedFootballers.txt"));
            for(int i = 0; i < MIDDLE_AGED_FOOTBALLERS.size(); i++) {
                pw.println("" + i + " " + MIDDLE_AGED_FOOTBALLERS.get(i));
            }
            pw.flush();
            pw.close();

            pw = new PrintWriter(new File(outputFilesDir, "oldAgeFootballers.txt"));
            for(int i = 0; i < OLD_AGE_FOOTBALLERS.size(); i++) {
                pw.println("" + i + " " + OLD_AGE_FOOTBALLERS.get(i));
            }

            pw.flush();
            pw.close();
        } catch (FileNotFoundException fnfe) {
            System.out.println("file for write not exist!");
        }
    }

    private static void sortFootballers(String key) {
        switch (key) {
            case "name": {
                Comparator<Footballer> nameSort = new Comparator<>() {
                    @Override
                    public int compare(Footballer f1, Footballer f2) {
                        int result = f1.getName().compareTo(f2.getName());
                        if (result != 0) {
                            return result;
                        } else {
                            result = f1.compareTo(f2);
                            if (result != 0) {
                                return result;
                            } else {
                                return Integer.compare(f1.getAge(), f2.getAge());
                            }
                        }
                    }
                };
                Collections.sort(YOUNG_AGE_FOOTBALLERS, nameSort);
                Collections.sort(MIDDLE_AGED_FOOTBALLERS, nameSort);
                Collections.sort(OLD_AGE_FOOTBALLERS, nameSort);
                break;
            }
            case "age": {
                Comparator<Footballer> ageSort = new Comparator<>() {
                    @Override
                    public int compare(Footballer f1, Footballer f2) {
                        int result = Integer.compare(f1.getAge(), f2.getAge());
                        if (result != 0) {
                            return result;
                        } else {
                            result = f1.compareTo(f2);
                            if (result != 0) {
                                return result;
                            } else {
                                return f1.getName().compareTo(f2.getName());
                            }
                        }
                    }
                };
                Collections.sort(YOUNG_AGE_FOOTBALLERS, ageSort);
                Collections.sort(MIDDLE_AGED_FOOTBALLERS, ageSort);
                Collections.sort(OLD_AGE_FOOTBALLERS, ageSort);
                break;
            }
            case "country": {
                Comparator<Footballer> countrySort = new Comparator<>() {
                    @Override
                    public int compare(Footballer f1, Footballer f2) {
                        int result = f1.getCountry().compareTo(f2.getCountry());
                        if (result != 0) {
                            return result;
                        } else {
                            result = f1.compareTo(f2);
                            if (result != 0) {
                                return result;
                            } else {
                                return Integer.compare(f1.getAge(), f2.getAge());
                            }
                        }
                    }
                };
                Collections.sort(YOUNG_AGE_FOOTBALLERS, countrySort);
                Collections.sort(MIDDLE_AGED_FOOTBALLERS, countrySort);
                Collections.sort(OLD_AGE_FOOTBALLERS, countrySort);
                break;
            }
        }
    }
}