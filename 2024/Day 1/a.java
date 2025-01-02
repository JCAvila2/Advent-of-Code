import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class a {
    public void result() throws IOException {
        String path = "input.txt";
        BufferedReader bfro = new BufferedReader(new FileReader(path));
        ArrayList<Integer> left_list = new ArrayList<Integer>();
        ArrayList<Integer> right_list = new ArrayList<Integer>();
        String st;
        while ((st = bfro.readLine()) != null) {
            String[] parts = st.split(" {3}");
            left_list.add(Integer.parseInt(parts[0]));
            right_list.add(Integer.parseInt(parts[1]));
        }

        Collections.sort(left_list);
        Collections.sort(right_list);

        int diff = 0;
        for (int i = 0; i < left_list.size(); i++) {
            diff += Math.abs(left_list.get(i) - right_list.get(i));
        }
        System.out.println("a: " + diff);
    }
}
