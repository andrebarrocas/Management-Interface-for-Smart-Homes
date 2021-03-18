package Controllers;

 
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;
import java.net.URL;
import java.util.ResourceBundle;

import Objects.LampBrandX;
import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.ColorPicker;
import javafx.scene.layout.Pane;


public class LampBrandXController implements PropertyChangeListener {
	
	
	/*
	 * 1 for OK, 0 for Err
	 */
	
	static LampBrandX lamp = LampBrandX.getInstance();
	
    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private Pane pane;

    @FXML
    private Button state;

    @FXML
    private ColorPicker rgb;

    @FXML
    void changeRGB(ActionEvent event) {
  
    }
    
    public void changeTheme() {
    	Platform.runLater(new Runnable() {
    	    @Override
    	    public void run() {
    	       	state.setText(lamp.buttonText);
    	    	pane.setStyle(lamp.background);
    	    }
    	});
 
    }

    
    @FXML
    public void changeState(ActionEvent event) {
    	lamp.setState();
    }
    	

    @FXML
    void initialize() {
    	state.setText("Ligar");
    	pane.setStyle("-fx-background-color: black");
    	lamp.addPropertyChangeListener(this);
    }


	@FXML
	public void propertyChange(PropertyChangeEvent evt) {
    	System.out.println("yeet");
    	changeTheme();
	}
    
}
