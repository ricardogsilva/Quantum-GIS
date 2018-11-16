#include "qgsmaplayerpropertiesbase.h"

QgsMapLayerPropertiesBase::QgsMapLayerPropertiesBase()
{

}

QgsMapLayerPropertiesBase::addPropertiesPageFactory( QgsMapLayerConfigWidgetFactory *factory )
{
    if ( !factory->supportsLayer(mLayer) || !factory->supportLayerPropertiesDialog() )
    {
      return;
    }

    QListWidgetItem *item = new QListWidgetItem();
    item->setIcon( factory->icon() );
    item->setText( factory->title() );
    item->setToolTip( factory->title() );

    mOptionsListWidget->addItem( item );

    QgsMapLayerConfigWidget *page = factory->createWidget( mLayer, nullptr, false, this );
    mLayerPropertiesPages << page;
    mOptionsStackedWidget->addWidget( page );
}
