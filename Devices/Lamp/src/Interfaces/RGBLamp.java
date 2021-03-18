package Interfaces;

public interface RGBLamp {
	

	//Setters
	public abstract int setState();
	public abstract int setRGB(String value);
	
	//Getters
	public abstract boolean getState();
	public abstract String getRGB();
	
	
}
