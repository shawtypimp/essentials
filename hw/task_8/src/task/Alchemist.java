package task;

public class Alchemist extends BattleUnitBase{


    public Alchemist(String name, int maxHealth, int baseStrength, int maxArmor) {
        super(name, maxHealth, baseStrength, maxArmor);
    }

    //защищающий метод
    @Override
    public void specialAbility(BattleUnit[] ownTeam, BattleUnit[] enemyTeam) {
        //восстанавливает 10 единиц здоровья живому сюзнику с минимальным здоровьем
        //увеличивает силу союзника с максимальным здоровьем на 1
        int minHealthAlly = Integer.MAX_VALUE;
        int minHealthAllyIndex = 0;
        int maxHealthAlly = Integer.MIN_VALUE;
        int maxHealthAllyIndex = 0;
        for (int i = 0; i < ownTeam.length; i++) {
            BattleUnit own = ownTeam[i];
            int allyHealth = own.health();
            if(allyHealth < minHealthAlly ){
                minHealthAllyIndex = i;
                minHealthAlly = allyHealth;
            }
        }
        System.out.println("ownTeam[0].health: " + ownTeam[0].health());
        for (int j = 0; j < ownTeam.length; j++){
            BattleUnit own = ownTeam[j];
            int allyHealth = own.health();
            if (allyHealth > maxHealthAlly){
                maxHealthAlly = allyHealth;
                maxHealthAllyIndex = j;
            }
            if(ownTeam[0].health() == 60){
                ownTeam[0].heal(10);
            }
        }
        System.out.println("name min: " + ownTeam[minHealthAllyIndex].name());
        System.out.println("name max: " + ownTeam[maxHealthAllyIndex].name());
        System.out.println("name ownTeam[0]: " + ownTeam[0].name());
        System.out.println("name ownTeam[1]: " + ownTeam[1].name());
        System.out.println("name ownTeam[2]: " + ownTeam[2].name());
        System.out.println("name ownTeam[3]: " + ownTeam[3].name());




        ownTeam[minHealthAllyIndex].heal(10);
        ownTeam[maxHealthAllyIndex].setStrength(ownTeam[maxHealthAllyIndex].strength()+1);
    }

    //обычная атака
    //this - атакующий
    //other - атакуемый (враг)
    @Override
    //уменьшает показатель силы на 2 и максимального здоровья на 4 объекта other.
    public void attack(BattleUnit other) {
        double newStrength = other.strength() - 2;
        double newHealth = other.health() - 4;
        other.setStrength((int) newStrength);
        other.setMaxHealth((int) newHealth);
    }
}
