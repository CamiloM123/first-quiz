package org.velezreyes.quiz.question6;

//Libraries
import java.util.HashMap;
import java.util.Map;

/**
 * Concrete implementation of the VendingMachine interface.
 * This class represents a vending machine that sells drinks.
 * 
 * @version 1.0.0
 * @author Camilo Muñoz
 * @see VendingMachine
 * @see Drink
 * @see NotEnoughMoneyException
 * @see UnknownDrinkException
 * @see DrinkImpl
 * @see VendingMachineImpl
 * @see DrinkTest
 */
public class VendingMachineImpl implements VendingMachine {
  private Map<String, Integer> drinkPrices;
  private int totalMoney;

  /**
   * Constructor for the VendingMachineImpl class.
   */
  private VendingMachineImpl() {
    drinkPrices = new HashMap<>();
    drinkPrices.put("ScottCola", 75);
    drinkPrices.put("KarenTea", 100);
  }

  /**
   * Getter for the instance property.
   * 
   * @return The instance of the VendingMachineImpl class.
   */
  public static VendingMachine getInstance() {
    return new VendingMachineImpl();
  }

  @Override
  public void insertQuarter() {
    totalMoney += 25;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    if (!drinkPrices.containsKey(name)) {
      throw new UnknownDrinkException(name);
    }


    int price = drinkPrices.get(name);
    
    if (totalMoney < price) {
      throw new NotEnoughMoneyException();
    }

    totalMoney -= price;

    return createDrink(name);
  }

  /**
   * Creates a Drink object.
   * 
   * @param name The name of the drink.
   * @return A Drink object.
   */
  private Drink createDrink(String name) {
    boolean isFizzy = name.equals("ScottCola");
    return new DrinkImpl(name, isFizzy);
  }
  
}
