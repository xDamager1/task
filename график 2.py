import numpy
import pylab
from matplotlib.widgets import Slider, RadioButtons, CheckButtons


def gauss(sigma, mu, x):
    ''' Отображаемая функция '''
    return (1.0 / (sigma * numpy.sqrt(2.0 * numpy.pi)) * numpy.exp(-((x - mu) ** 2) / (2 * sigma * sigma)))


if __name__ == '__main__':
    def updateGraph():
        ''' Функция для обновления графика '''
        global slider_sigma
        global slider_mu
        global graph_axes
        global radiobuttons_color
        global grid_visible

        colors = {'Красный': 'r', 'Синий': 'b', 'Зелёный': 'g'}

        sigma = slider_sigma.val
        mu = slider_mu.val
        p = point.val
        x = numpy.arange(-5.0, 5.0, 0.01)
        y = gauss(sigma, mu, x)

        style = colors[radiobuttons_color.value_selected]

        graph_axes.clear()
        graph_axes.plot(x, y, style)

        if grid_visible:
            graph_axes.grid()
        pylab.draw()


    def onChangeGraph(value):
        ''' Обработчик события изменения значений слайдеров '''
        updateGraph()


    def onRadioButtonsClicked(label):
        ''' Обработчик события при клике по RadioButtons '''
        updateGraph()


    def onCheckClicked(label):
        ''' !!! Обработчик события при клике по CheckButtons '''
        global grid_visible
        if label == 'Сетка':
            grid_visible = not grid_visible
        updateGraph()


    fig, graph_axes = pylab.subplots()
    graph_axes.grid()

    grid_visible = True

    fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.55)

    axes_slider_sigma = pylab.axes([0.05, 0.35, 0, 85, 0.04])
    slider_sigma = Slider(axes_slider_sigma, label='', valmin=0.1, valmax=1.0, valinit=0.5, valfmt='%1.2f')

    slider_sigma.on_changed(onChangeGraph)

    axes_slider_mu = pylab.axes([0.05, 0.27, 0.85, 0.04])
    slider_mu = Slider(axes_slider_mu, label='', valmin=-4.0, valmax=4.0, vainit=0.0, valfmt='%1.2f')

    # Слайдер, премещение которого приводит в движение точку на кривой
    axpoint = pylab.axes([0.25, 0.2, 0.65, 0.03])
    point = Slider(axpoint, label='', valmin=-3.0, valmax=3.0, valinit=0.2, valfmt='%1.2f')


    # Кнопка, которая возвращает точку в начальное положение
    def reset_h():
        point.val = point


    reset_button = Button(description='Вернуть точку в начальное положение')
    reset_button.on_click(reset_h)

    # Радионопка для ищменения цвета и стиля графика
    color = RadioButtons(options=['purple', 'yellow', 'red', 'green'], value='purple', description='Цвет грфика')
    style = RadioButtons(options=['-', '--', ':', '-.'], value='-', description='Стиль грфика')

    # Флажок включающий и выключающий касательную к графику
    var = BooleanVar()
    cb = Checkbutton(self, text="Text", variable=var, command=self.onClick)

    state = var.get()  # Получаем состояние (True — включено, False — выключено)
    var.set(True)  # Включаем флажок
    var.set(False)  # Выключаем флажок

    slider_mu.on_changed(onChangeGraph)

    axes_radiobuttons = pylab.axes([0.05, 0.05, 0.2, 0.2])

    radiobuttons_color = RadioButtons(axes_radiobuttons, ['Красный', 'Синий', 'Зелёный'])
    radiobuttons_color.on_clicked(onRadioButtonsClicked)

    axes_checkbuttons = pylab.axes([0.35, 0.15, 0.2, 0.1])

    checkbutton_grid = CheckButtons(axes_checkbuttons, ['Сетка'], [True])
    checkbutton_grid.on_clicked(onCheckClicked)

    updateGraph()
    pylab.show()