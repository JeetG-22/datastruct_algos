package arrays;

public class BagRunner {
    public static void main(String[] args){
        Bag<Integer> bagInt = new Bag<>();
        bagInt.add(10);
        bagInt.add(25);
        bagInt.add(1478081);
        bagInt.add(Integer.MAX_VALUE);
        bagInt.add(Integer.MIN_VALUE);

        System.out.println("Bag of Integers:");
        for(Integer x : bagInt){
            System.out.println(x);
        }
        System.out.println();

        System.out.println("Bag of Doubles:");
        Bag<Double> bagDouble = new Bag<>();
        bagDouble.add(Double.POSITIVE_INFINITY);
        bagDouble.add(Double.NEGATIVE_INFINITY);

        for(Double x : bagDouble){
            System.out.println(x);
        }

    }
}
