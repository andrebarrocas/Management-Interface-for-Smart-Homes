package Objects;
import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;
import java.util.Observable;

import Interfaces.RGBLamp;

/*
 * I'm lazy, um DTO seria mais eficiente mas isto é só para
 * testes so why not carregar o objeto e lidar com dados na 
 * mesma classe ahah
 */
public class LampBrandX implements RGBLamp  {
	
    private PropertyChangeSupport changes = new PropertyChangeSupport(this);
	
	private static LampBrandX singleton = null;
		
	/*
	 * 1 for OK, 0 for Err
	 */
	
	private Boolean state = false;
	private String RGB;
	
	public String background;
	public String buttonText;;
	
	private LampBrandX() {
	}
	
	public static LampBrandX getInstance() {
		if (singleton == null) singleton = new LampBrandX();
		return singleton;
	}
	
	public int setState() {
		if(state) {
			this.state = false;
			this.background = "-fx-background-color: black";
			this.buttonText = "Ligar";
			changes.firePropertyChange("state",true,false);
		} else {
			this.state = true;
			this.background = "-fx-background-color: yellow";
			this.buttonText = "Desligar";
			changes.firePropertyChange("state",false,true);;

		}
		return 1;
	}

	public boolean getState() {
		return state;
	}

	public int setRGB (String value) {
		this.RGB = value;
		return 1;
	}

	public String getRGB() {
		return RGB;
	}

	  public void addPropertyChangeListener(PropertyChangeListener l) {
	        changes.addPropertyChangeListener(l);
	    }

	    public void removePropertyChangeListener(PropertyChangeListener l) {
	        changes.removePropertyChangeListener(l);
	    }
}
