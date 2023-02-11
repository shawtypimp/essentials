public class ATM {
   private int ten_$;
    private int twelve_$;
    private int fifty_$;
    private int one_hundred_$;

    private int total_count;

    public ATM(int ten_$, int twelve_$, int fifty_$, int one_hundred_$){
        this.ten_$ = 10;
        this.twelve_$ = 20;
        this.fifty_$ = 50;
        this.one_hundred_$ = 100;
    }

    public int getTen_$() {
        return ten_$;
    }

    public void setTen_$(int ten_$) {
        this.ten_$ = ten_$;
    }

    public int getTwelve_$() {
        return twelve_$;
    }

    public void setTwelve_$(int twelve_$) {
        this.twelve_$ = twelve_$;
    }

    public int getFifty_$() {
        return fifty_$;
    }

    public void setFifty_$(int fifty_$) {
        this.fifty_$ = fifty_$;
    }

    public int getOne_hundred_$() {
        return one_hundred_$;
    }

    public void setOne_hundred_$(int one_hundred_$) {
        this.one_hundred_$ = one_hundred_$;
    }

    public void load(int ten_$, int twelve_$, int fifty_$, int one_hundred_$ ){
        this.total_count+= ten_$ + twelve_$ + fifty_$ + one_hundred_$;
    }
    public boolean give(int sum) {
        if (sum % 10 != 0) {
            return false;
        }
        if (sum > one_hundred_$) {
            one_hundred_$ -= sum / 100;
            sum -= (sum / 100) * 100;
            }
        if (sum > fifty_$) {
            fifty_$ -= sum / 50;
            sum -= (sum / 50) * 50;
        }
        if (sum > twelve_$) {
            twelve_$ -= sum / 20;
            sum -= (sum / 20) * 20;
        }
        if (sum > ten_$) {
            ten_$ -= sum / 10;
            sum -= (sum / 10) * 10;
        }
        if(sum !=0){
        return true;
        }
        else{
            return false;
        }
    }

}