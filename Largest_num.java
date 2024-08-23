public class Largest_num{
    public static void main(String args[]){
        int arr[]={1,4,5,6,17,9};
        int max=arr[0];

        for (int i=1;i<arr.length;i++){
            if (arr[i]>max){
                max=arr[i];
            }
        }
        System.out.println(max);
    }
}