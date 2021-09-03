import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

public class Practice {
    public static void main(String[] args) {
//        charCount();
//        intReverse();
//        stringReverse();
        sentenceReverse();
    }

    /**
     * sentence reverse
     */
    public static void sentenceReverse() {
        Scanner s = new Scanner(System.in);
        ArrayList<String> newStr = new ArrayList<>();
        String[] array = s.nextLine().split(" ");
        for (int i = array.length; i > 0 ; i--) {
            newStr.add(array[i - 1]);
        }
        System.out.println(String.join(" ", newStr));
    }

    /**
     * string reverse
     */
    public static void stringReverse() {
        Scanner s = new Scanner(System.in);
        StringBuilder newStr = new StringBuilder(100);
        char[] array = s.nextLine().toCharArray();
        for (int i = array.length; i > 0 ; i--) {
            newStr.append(Array.get(array, i - 1));
        }
        System.out.println(newStr);
    }

    /**
     * integer reverse
     */
    public static void intReverse() {
        Scanner s = new Scanner(System.in);
        StringBuilder newStr = new StringBuilder(100);
        char[] array = s.nextLine().toCharArray();
        for (int i = array.length; i > 0 ; i--) {
            newStr.append(Array.get(array, i - 1));
        }
        System.out.println(newStr);
    }
    /**
     * Statistics on the number of non duplicate strings
     */
    public static void charCount() {
        HashSet<Integer> set = new HashSet<>();
        Scanner s =new Scanner(System.in);
        String str = s.nextLine();
        char[] array = str.toCharArray();
        for(char ch : array){
            if((int) ch <=127){
                set.add((int) ch);
            }
        }
        System.out.println(set.size());
    }


}
