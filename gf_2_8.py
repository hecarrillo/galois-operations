''' 
The following program computes the multiplication
between two 8 bit numbers in GF(2⁸), this means that 
given A(x) and B(x) inputted in hex by the user, 
it outputs C(x) = A(x) * B(x) mod P(x) where P(x) is an
irreducible polynomial (0x11B)
'''
import wx

def gf_mult(a, b):
    result = 0
    for bit in range(8):
        if b & (1 << bit):
            result ^= a << bit
    for bit in range(15, 7, -1):
        if result & (1 << bit):
            result ^= 0x11B << (bit - 8)
    return result & 0xFF

class GF2nFrame(wx.Frame):
    def __init__(self, parent, title):
        super(GF2nFrame, self).__init__(parent, title=title, size=(350, 200))
        self.panel = wx.Panel(self)
        self.init_ui()

    def init_ui(self):
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self.panel, label='A (hex):')
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        self.a_input = wx.TextCtrl(self.panel)
        hbox1.Add(self.a_input, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(self.panel, label='B (hex):')
        hbox2.Add(st2, flag=wx.RIGHT, border=8)
        self.b_input = wx.TextCtrl(self.panel)
        hbox2.Add(self.b_input, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        calc_btn = wx.Button(self.panel, label='Calculate')
        hbox3.Add(calc_btn)
        self.result_text = wx.StaticText(self.panel, label='')
        hbox3.Add(self.result_text, flag=wx.LEFT, border=10)
        vbox.Add(hbox3, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        calc_btn.Bind(wx.EVT_BUTTON, self.on_calc)

        self.panel.SetSizer(vbox)

    def on_calc(self, event):
        a_hex = self.a_input.GetValue()
        b_hex = self.b_input.GetValue()
        try:
            a = int(a_hex, 16)
            b = int(b_hex, 16)
            result = gf_mult(a, b)
            self.result_text.SetLabel(f'Result: {result:02X}')
        except ValueError:
            wx.MessageBox('Please enter valid hexadecimal numbers', 'Error', wx.OK | wx.ICON_ERROR)

if __name__ == '__main__':
    app = wx.App(False)
    frame = GF2nFrame(None, title='GF(2^8) Multiplication')
    frame.Show()
    app.MainLoop()
