/***************************************************************************
                          qgsmaplayerpropertiesbase.h
                   Base class for all layer properties dialogs
                             -------------------
    begin                : 2018-10-29
    copyright            : (C) 2018 by Ricardo Garcia Silva
    email                : ricardo.garcia.silva at gmail.com
***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

#ifndef QGSMAPLAYERPROPERTIESBASE_H
#define QGSMAPLAYERPROPERTIESBASE_H

#include "qgsoptionsdialogbase.h"
#include "qgsmaplayer.h"

class QgsMapLayer;
class QgsMapLayerConfigWidgetFactory;

class APP_EXPORT QgsMapLayerPropertiesBase :
{
  public:
    QgsMapLayerPropertiesBase( QgsMapLayer *layer = nullptr);

    //! Adds a properties page factory to the vector layer properties dialog.
    void addPropertiesPageFactory( QgsMapLayerConfigWidgetFactory *factory );
};

#endif // QGSMAPLAYERPROPERTIESBASE_H
