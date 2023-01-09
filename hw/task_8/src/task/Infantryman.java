package task;

public class Infantryman extends BattleUnitBase {

    public Infantryman(String name, int maxHealth, int baseStrength, int maxArmor) {
        super(name, maxHealth, baseStrength, maxArmor);
    }

    @Override
    public void specialAbility(BattleUnit[] ownTeam, BattleUnit[] enemyTeam) {
    }

    @Override
    //если противник в броне (+),наносит повреждения по здоровью, равные половине силы (+),
    //и повреждения по броне равные четверти силы, (+) иначе
    //наносит повреждения здоровью, равные силе. (+)
    //минимальные повреждения любого типа - 1
            //this. - атакующий
            //attacker. - атакуемый
            //все изменения в характеристиках делаются через методы из BattleUnitBase
    public void attack(BattleUnit attacker) {
        double halfAttack = (this.strength / 2);
        double quarterAttack = (this.strength / 4);
        if(halfAttack < 1) halfAttack=1;
        if(quarterAttack < 1) quarterAttack=1;
        if(attacker.armor()==0) {
            attacker.takeDamage(this.strength);
        } else {
            attacker.takeDamage((int) halfAttack);
            attacker.damageArmor((int) quarterAttack);
        }
    }
}