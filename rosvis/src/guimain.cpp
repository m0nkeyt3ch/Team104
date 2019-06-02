/**
 * @file /src/main.cpp
 *
 * @brief Qt based gui.
 *
 * @date November 2010
 **/
/*****************************************************************************
** Includes
*****************************************************************************/

#include <QtGui>
#include <QApplication>
#include "../include/rosvis/main_window.hpp"
#include "../include/rosvis/gui.h"

/*****************************************************************************
** Main
*****************************************************************************/

int startGUI(int argc, char **argv) {

    /*********************
    ** Qt
    **********************/
    QApplication app(argc, argv);

    rosvis::MainWindow w(argc,argv);
    w.show();
    app.connect(&app, SIGNAL(lastWindowClosed()), &app, SLOT(quit()));
    int result = app.exec();

    return result;
}
