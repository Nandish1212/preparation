class reversing_num{
    public static void main(String args[]){
        int num = 12345,reversed=0;
        while(num!=0){
            int digit=num%10;
            reversed=reversed*10+digit;
            num=num/10;
        }
        System.out.println("Reversed number is: "+reversed);
    }
}