import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class b {
    public void result() throws IOException {
        String path = "input.txt";
        BufferedReader bfro = new BufferedReader(new FileReader(path));
        ArrayList<Integer> left_list = new ArrayList<Integer>();
        Map<Integer, Integer> right_list = new HashMap<>();
        String st;
        while ((st = bfro.readLine()) != null) {
            String[] parts = st.split(" {3}");
            left_list.add(Integer.parseInt(parts[0]));
            int right_number = Integer.parseInt(parts[1]);
            if (!right_list.containsKey(right_number)) {
                right_list.put(right_number, 1);
            } else {
                right_list.put(right_number, right_list.get(right_number) + 1);
            }
        }

        int total = 0;
        for (int actual : left_list) {
            int repetitions = 0;
            if (right_list.containsKey(actual)) {
                repetitions = right_list.get(actual);
            }
            total += actual * repetitions;
        }
        System.out.println("b: " + total);
    }
}
