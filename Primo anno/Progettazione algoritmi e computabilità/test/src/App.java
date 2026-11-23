import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("--- Esempi fase implementativa ---");

        List S = new ArrayList<Integer>();
        S.add(4);

    }

    // metodi dal meno efficente al più efficente
    // Return true se la List contiene un duplicato, altrimenti false

    // complessità O(n^3)
    public static boolean verificaDupList1(List S) {
        for (int i=0; i< S.size(); i++){
            Object x = S.get(i);
            for (int j = i + 1 ; j<S.size(); j++){
                Object y = S.get(i);
                if(x.equals(y)){
                    return true;
                }
            }
        }

        return false;
    }

    // Stesso metodo, complessità massima di O(N^2)
    // il get in java puà potenzialmente portare ad una complessità maggiore
    public static boolean verificaDupList2(List S){
        Object[] array = S.toArray();
        for (int i=0; i< array.length; i++){
            Object x = array[i];
            for (int j = i + 1 ; j<array.length; j++){
                Object y = array[j];
                if(x.equals(y)){
                    return true;
                }
            }
        }

        return false;
}

}
