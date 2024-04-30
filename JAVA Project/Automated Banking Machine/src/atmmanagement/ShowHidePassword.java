package atmmanagement;

import javax.swing.JPasswordField;
import javax.swing.JTextField;

public class ShowHidePassword {
	public void showPassword(JPasswordField passField, JTextField textField) {
		String password = passField.getText();
		passField.setVisible(false);		
		textField.setVisible(true);
		textField.setText(password);		
	}
	
	public void hidePassword(JPasswordField passField, JTextField textField) {
		String password = textField.getText();
		textField.setVisible(false);		
		passField.setVisible(true);
		passField.setText(password);		
	}
}
