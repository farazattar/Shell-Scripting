private void TextBox_GotFocus(object sender, RoutedEventArgs e)
{
    TextBox textBox = (TextBox)sender;
    if (textBox.Text == "Enter your value here")
    {
        textBox.Text = string.Empty;
    }
}

private void TextBox_LostFocus(object sender, RoutedEventArgs e)
{
    TextBox textBox = (TextBox)sender;
    if (string.IsNullOrWhiteSpace(textBox.Text))
    {
        textBox.Text = "Enter your value here";
    }
}
