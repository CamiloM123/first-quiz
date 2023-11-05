package org.velezreyes.quiz.question6;

/**
 * Concrete implementation of the Drink interface.
 * This class represents a beverage with a name and a property to indicate if it's fizzy.
 * 
 * @version 1.0.0
 * @author Camilo Muñoz
 * @see Drink
 */
public class DrinkImpl implements Drink {
    private String name; 
    private boolean isFizzy;

    /**
     * Constructor for the DrinkImpl class.
     * 
     * @param name The name of the drink.
     * @param isFizzy A boolean indicating if the drink is fizzy.
     */
    public DrinkImpl(String name, boolean isFizzy) {
        this.name = name; 
        this.isFizzy = isFizzy;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public boolean isFizzy() {
        return isFizzy;
    }
}
