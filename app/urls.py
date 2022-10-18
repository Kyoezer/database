from django.urls import path
from. import views

urlpatterns = [
    path('home/', views.home, name="home"),

    path('portfolio/', views.portfolio, name="portfolio"),
  
    path('base/', views.base, name="base"),
    path('stat/', views.stat, name="stat"),
    path('', views.index, name="index"),
    path('postupdate/<int:pk>/', views.postupdate, name="postupdate"),
    
  

    path('user_pro/', views.user_pro, name="user_pro"),
    path('notapproved/', views.notapproved, name="notapproved"),
    path('approved/', views.approved, name="approved"),
    path('reject/', views.reject, name="reject"),
    path('editpro/', views.editpro, name="editpro"),
    path('proupdate/', views.proupdate, name="proupdate"),
    path('profile/', views.profile, name="profile"),
    path('heriages/', views.heriages, name='heriages'),
    path('heritagenotauth/', views.heritagenotauth, name='heritagenotauth'),
    path('arts/', views.arts, name='arts'),
    path('artauth/', views.artauth, name='artauth'),
    path('media/', views.media, name='media'),
    path('authmedia/', views.authme, name='authmedia'),
    path('creation/', views.creation, name='creation'),
    path('creationauth/', views.creationauth, name='creationauth') ,

    path('artist/', views.artist, name='artist'), 
    path('artistdetil/<int:pk>/',views.artistdetil.as_view(), name="artistdetil"),
    path('delete/<int:pk>/', views.delete, name="delete"),
    
    path('event/', views.event, name='event'),
    path('eventupdate/', views.eventupdate, name="eventupdate"), 

    path('showevent/', views.showevent, name="showevent"),
    path('eventdetil/<int:pk>/', views.eventdetil, name="eventdetil"),
    path('eventdetil/<int:pk>/contact_view/', views.contact_view, name="contact_view"), 

    path('aboutus/', views.aboutus, name="aboutus"),
    path('contactadmin/', views.contactadmin, name="contactadmin"),
    path('industries/', views.industries, name="industries"), 
    path('artstype/', views.artstype, name="artstype"),

    path('artc/', views.artc, name="artc"),

    path('search/', views.search, name="search"),
    path('policy/', views.policy, name="policy"), 
    path('terms/', views.terms, name="terms"), 

    # artspost
    path('artspost/', views.artspost, name="artspost"),
    path('artsauth/', views.artsauth, name="artsauth"),

    path('festival/', views.festival, name="festival"), 

    # festival
    path('festivalspost/', views.festivalpost, name="festivalpost"),
    path('festivalauth/', views.festivalauth, name="festivalauth"),

    path('cel/', views.cel, name="cel"),

     # celebration
    path('celepost/', views.celepost, name="celepost"),
    path('celeauth/', views.celeauth, name="celeauth"),

    path('histo/', views.histo, name="histo"),

    # historical
    path('histopost/', views.histopost, name="histopost"),
    path('histoauth/', views.histoauth, name="histoauth"),


    path('muse/', views.muse, name="muse"),
    # muse
    path('muspost/', views.muspost, name="muspost"),
    path('musauth/', views.musauth, name="musauth"),
    
    path('labri/', views.labri, name="labri"),
    # labrares
    path('labpost/', views.labpost, name="labpost"),
    path('labauth/', views.labauth, name="labauth"),


    path('achi/', views.achi, name="achi"),
    # archives
    path('archspost/', views.archspost, name="archspost"),
    path('archauth/', views.archauth, name="archauth"),


    path('paint/', views.paint, name="paint"),
     # painting
    path('paintpost/', views.paintpost, name="paintpost"),
    path('paintauth/', views.paintauth, name="paintauth"),

    path('digi/', views.digi, name="digi"),
    # painting
    path('digitalpost/', views.digitalpost, name="digitalpost"),
    path('digitalauth/', views.digitalauth, name="digitalauth"),

    path('photo/', views.photo, name="photo"),
    # photography
    path('photopost/', views.photopost, name="photopost"),
    path('photoauth/', views.photoauth, name="photoauth"),

    path('scul/', views.scul, name="scul"),
     # photography
    path('sculpost/', views.sculpost, name="sculpost"),
    path('sculauth/', views.sculauth, name="sculauth"),

    path('pott/', views.pott, name="pott"),
     # pottry
    path('potpost/', views.potpost, name="potpost"),
    path('potauth/', views.potauths, name="potauth"),

    path('liv/', views.liv, name="liv"),
    # pottry
    path('livepost/', views.livepost, name="livepost"),
    path('liveauth/', views.liveauth, name="liveauth"),

    path('thea/', views.thea, name="thea"),
    # pottry
    path('thepost/', views.thepost, name="thepost"),
    path('theauth/', views.theauth, name="theauth"),

    path('dan/', views.dan, name="dan"),
    # pottry
    path('dancepost/', views.dancepost, name="dancepost"),
    path('danceauth/', views.danceauth, name="danceauth"),

    path('ope/', views.ope, name="ope"),
     # pottry
    path('oppost/', views.oppost, name="oppost"),
    path('opauth/', views.opauth, name="opauth"),

    path('pup/', views.pup, name="pup"),
     # pup
    path('puppost/', views.puppost, name="puppost"),
    path('pupauth/', views.pupauth, name="pupauth"),

    path('book/', views.book, name="book"),
     # pup
    path('bookpost/', views.bookpost, name="bookpost"),
    path('bookauth/', views.bookauth, name="bookauth"),

    path('maga/', views.maga, name="maga"),
     # pup
    path('magapost/', views.magapost, name="magapost"),
    path('magaauth/', views.magaauth, name="magaauth"),

    path('com/', views.com, name="com"),
     # com
    path('compost/', views.compost, name="compost"),
    path('comauth/', views.comauth, name="comauth"),

    path('fil/', views.fil, name="fil"),
     # fil
    path('filpost/', views.filpost, name="filpost"),
    path('filauth/', views.filauth, name="filauth"),

    path('tele/', views.tele, name="tele"),
     # fil
    path('telepost/', views.telepost, name="telepost"),
    path('teleauth/', views.teleauth, name="teleauth"),

    path('rad/', views.rad, name="rad"),
     # fil
    path('radpost/', views.radpost, name="radpost"),
    path('radauth/', views.radauth, name="radauth"),

    path('musv/', views.musv, name="musv"),
    # fil
    path('mvpost/', views.mvpost, name="mvpost"),
    path('mvauth/', views.mvauth, name="mvauth"),

    path('digicon/', views.digicon, name="digicon"),
     # fil
    path('dcpost/', views.dcpost, name="dcpost"),
    path('dcauth/', views.dcauth, name="dcauth"),

    path('soft/', views.soft, name="soft"),
     # fil
    path('softpost/', views.softpost, name="softpost"),
    path('softauth/', views.softauth, name="softauth"),

    path('videogame/', views.videogame, name="videogame"),
    # fil
    path('vgpost/', views.vgpost, name="vgpost"),
    path('anauth/', views.vgauths, name="anauth"),

    path('anima/', views.anima, name="anima"),
    # fil
    path('anpost/', views.anpost, name="anpost"),
    path('anauth/', views.anauths, name="anauth"),

    path('fas/', views.fas, name="fas"),
    # fil
    path('fepost/', views.fepost, name="fepost"),
    path('authfe/', views.authfe, name="authfe"),

    path('jewe/', views.jewe, name="jewe"),
    # fil
    path('jewpost/', views.jewpost, name="jewpost"),
    path('authjew/', views.authjew, name="authjew"),

    path('toy/', views.toy, name="toy"),
    # fil
    path('toypost/', views.toypost, name="toypost"),
    path('authtoy/', views.authtoy, name="authtoy"),

    path('inte/', views.inte, name="inte"),
     # fil
    path('setpost/', views.setpost, name="setpost"),
    path('authset/', views.authset, name="authset"),

    path('graph/', views.graph, name="graph"),
    # fil
    path('grapost/', views.grapost, name="grapost"),
    path('authgra/', views.authgra, name="authgra"),


    path('arch/', views.arch, name="arch"),
    # fil
    path('archpost/', views.archpost, name="archpost"),
    path('autharch/', views.autharc, name="autharch"),

    path('adver/', views.adver, name="adver"),
    # fil
    path('adpost/', views.adpost, name="adpost"),
    path('authad/', views.authad, name="authad"),

    path('creative/', views.creative, name="creative"),
     # fil
    path('crdpost/', views.crdpost, name="crdpost"),
    path('authcrd/', views.authcrd, name="authcrd"),

    path('ser/', views.ser, name="ser"),
     # fil
    path('cespost/', views.cespost, name="cespost"),
    path('authces/', views.authce, name="authces"),

    path('digicreative/', views.digicreative, name="digicreative"),
    # fil
    path('digpost/', views.digpost, name="digpost"),
    path('authdig/', views.authdig, name="authdig"),


]

