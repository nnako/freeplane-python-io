<map version="freeplane 1.3.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<attribute_registry SHOW_ATTRIBUTES="hide"/>
<node FOLDED="false" ID="ID_272918048" CREATED="1438501233609" MODIFIED="1552467104508" LINK="file:/C:/Users/Nnamdi/01%20-%20PROJEKTE/Freeplane/Freeplane.mm#ID_349830097"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p style="text-align: center">
      PYTHON API
    </p>
    <p style="text-align: center">
      to access Freeplane files
    </p>
  </body>
</html>
</richcontent>
<edge STYLE="horizontal" COLOR="#cccccc"/>
<hook NAME="MapStyle" zoom="0.564">
    <properties show_icon_for_attributes="false" show_note_icons="true"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node">
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right">
<stylenode LOCALIZED_TEXT="default">
<font NAME="Segoe UI" SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.note"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="12" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="12" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="12" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
<stylenode TEXT="klein und grau" COLOR="#999999">
<font SIZE="10"/>
</stylenode>
<stylenode TEXT="NEGATIV (rot)" COLOR="#ff0000"/>
<stylenode TEXT="POSITIV (gr&#xfc;n)" COLOR="#338800"/>
<stylenode TEXT="ANFORDERUNG (extern)" BACKGROUND_COLOR="#ffcc00"/>
<stylenode TEXT="DETAILDARSTELLUNG" BACKGROUND_COLOR="#ccccff"/>
<stylenode TEXT="ANFORDERUNG (intern)" BACKGROUND_COLOR="#ffff00"/>
<stylenode TEXT="RISIKO" BACKGROUND_COLOR="#ff6600"/>
<stylenode TEXT="DOKUMENTATION" BACKGROUND_COLOR="#ccffcc"/>
<stylenode TEXT="gelb und fett" COLOR="#999999" BACKGROUND_COLOR="#fce99d"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000">
<font SIZE="20"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="12"/>
</stylenode>
</stylenode>
</stylenode>
</map_styles>
</hook>
<node TEXT="scope" STYLE_REF="klein und grau" POSITION="right" ID="ID_568512651" CREATED="1510406410324" MODIFIED="1552467114786" MIN_WIDTH="80">
<node TEXT="API for handling mindmaps (Freemind, Freeplane,...)" ID="ID_290364692" CREATED="1510406411746" MODIFIED="1510406445146"/>
</node>
<node TEXT="benefits" STYLE_REF="klein und grau" POSITION="right" ID="ID_1141471719" CREATED="1542292423233" MODIFIED="1552467114786" MIN_WIDTH="80">
<node TEXT="NO dependencies / issues concerning JAVA updates" ID="ID_1017052286" CREATED="1542292427234" MODIFIED="1542292460595"/>
<node TEXT="NO JAVA RTE needed to access freeplane &quot;database&quot;" ID="ID_1435094044" CREATED="1542292463353" MODIFIED="1542292493515"/>
<node TEXT="cross-platform accessibility of mindmap file" ID="ID_1738899901" CREATED="1542292496383" MODIFIED="1611227259775"/>
<node TEXT="risk-free edit of underlying XML structure" ID="ID_783298030" CREATED="1611227225092" MODIFIED="1611227276201">
<node TEXT="manual edit of mm-file is prone to destruction of structure" STYLE_REF="klein und grau" ID="ID_538588006" CREATED="1611227276215" MODIFIED="1611227300159"/>
</node>
<node TEXT="..." STYLE_REF="klein und grau" ID="ID_96881121" CREATED="1542292552103" MODIFIED="1542292553215"/>
</node>
<node TEXT="UI" STYLE_REF="klein und grau" POSITION="right" ID="ID_1371414909" CREATED="1510395289460" MODIFIED="1552467114786" MIN_WIDTH="80">
<node TEXT="[ CLI ]" ID="ID_1245010117" CREATED="1510517874653" MODIFIED="1510517878740">
<node ID="ID_1920490854" CREATED="1510549877347" MODIFIED="1522321676754"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    &gt; python<b>&#160;freeplane.py </b><font color="#0000ff">&lt;path&gt;</font><b>&#160;</b><font color="#0000ff">[</font><b>&#160;</b><font color="#0000ff">&lt;option&gt;</font><b>&#160;</b><font color="#0000ff">]*</font>
  </body>
</html>
</richcontent>
<node TEXT="&lt;path&gt;" STYLE_REF="klein und grau" ID="ID_1047494501" CREATED="1510549877362" MODIFIED="1510549877378">
<node TEXT="filepath to mindmap" ID="ID_1468660501" CREATED="1510549891756" MODIFIED="1510549898943"/>
</node>
<node TEXT="&lt;option&gt;" STYLE_REF="klein und grau" ID="ID_1947109182" CREATED="1510549877378" MODIFIED="1510549877378">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1732876992" CREATED="1510549901143" MODIFIED="1510549903302">
<node TEXT="..." ID="ID_1545663694" CREATED="1510549903302" MODIFIED="1510549904286"/>
</node>
</node>
</node>
<node TEXT="example" STYLE_REF="klein und grau" ID="ID_158700351" CREATED="1510550060222" MODIFIED="1510550063226">
<node TEXT="[ HOME ]" STYLE_REF="klein und grau" FOLDED="true" ID="ID_1193775787" CREATED="1510407616008" MODIFIED="1510407619144">
<node TEXT="ENV_python27\Scripts\activate" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_694209516" CREATED="1504785938818" MODIFIED="1510407632195"/>
<node TEXT="c:" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_684920997" CREATED="1504785966355" MODIFIED="1510407636165"/>
<node TEXT="cd c:\Users\nnamdi\02 - TOOLS\_Python\LIB__freeplane" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_564775093" CREATED="1504785981635" MODIFIED="1541677372849"/>
</node>
<node TEXT="[ WORK ]" STYLE_REF="klein und grau" ID="ID_1231830388" CREATED="1510407621998" MODIFIED="1510407623918">
<node TEXT="ENV__Python27\Scripts\activate" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_286439503" CREATED="1504785938818" MODIFIED="1504785942195"/>
<node TEXT="ENV__Python27\Scripts\activate" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_124486206" CREATED="1504785938818" MODIFIED="1504785942195"/>
<node TEXT="c:" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_246033847" CREATED="1510407717798" MODIFIED="1587363715806"/>
<node TEXT="cd c:\Users\pkohn\_NEXTCLOUD\_TOOLS\_Python\LIB__freeplane" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_919313793" CREATED="1510407726674" MODIFIED="1587363739775"/>
<node TEXT="python -m pdb example.py" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_326787135" CREATED="1510407726674" MODIFIED="1552494354841"/>
</node>
</node>
</node>
<node TEXT="[ API ]" ID="ID_1823383479" CREATED="1510517879676" MODIFIED="1510517885010">
<node TEXT="see code" STYLE_REF="klein und grau" ID="ID_473462955" CREATED="1510552768566" MODIFIED="1510552778922" LINK="#ID_1739128016"/>
</node>
</node>
<node TEXT="FILES" STYLE_REF="klein und grau" POSITION="right" ID="ID_134346911" CREATED="1505557531697" MODIFIED="1608708070543" MIN_WIDTH="80">
<node TEXT="freeplane.py" STYLE_REF="DOKUMENTATION" ID="ID_1934554825" CREATED="1505557547296" MODIFIED="1608708102620" LINK="freeplane.py">
<font BOLD="false"/>
<node TEXT="scope" STYLE_REF="klein und grau" ID="ID_339480285" CREATED="1510395217606" MODIFIED="1583832904158" MIN_WIDTH="60">
<node TEXT="..." ID="ID_85604639" CREATED="1510395220118" MODIFIED="1510395220884"/>
</node>
<node TEXT="/" ID="ID_1739128016" CREATED="1505560809647" MODIFIED="1505560810367">
<node TEXT="freeplane" ID="ID_1802543342" CREATED="1552496009277" MODIFIED="1552496012266">
<font BOLD="true"/>
<node TEXT="." ID="ID_1255487056" CREATED="1562187733944" MODIFIED="1562187737441">
<node ID="ID_694394550" CREATED="1562187851914" MODIFIED="1562187851914"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">string </font><b>= ICON_EXCLAMATION</b>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1974092981" CREATED="1562187851914" MODIFIED="1562187851914"/>
</node>
</node>
<node TEXT="." ID="ID_1843515383" CREATED="1562187747608" MODIFIED="1562187748596">
<node ID="ID_1546285578" CREATED="1562187851898" MODIFIED="1562187851898"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">string </font><b>= ICON_LIST</b>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_769673032" CREATED="1562187851898" MODIFIED="1562187851898"/>
</node>
</node>
<node TEXT="." ID="ID_1119841633" CREATED="1562187753782" MODIFIED="1562187754768">
<node ID="ID_1884395811" CREATED="1562187851883" MODIFIED="1562187851898"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">string </font><b>= ICON_QUESTION</b>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_595358047" CREATED="1562187851898" MODIFIED="1562187851898"/>
</node>
</node>
<node TEXT="." ID="ID_290784877" CREATED="1562187760316" MODIFIED="1562187761345">
<node ID="ID_1176467863" CREATED="1562187851883" MODIFIED="1562187851883"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">string </font><b>= ICON_CHECKED</b>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_363647842" CREATED="1562187851883" MODIFIED="1562187851883"/>
</node>
</node>
<node TEXT="." ID="ID_318506863" CREATED="1562187768233" MODIFIED="1562187769392">
<node ID="ID_653720668" CREATED="1562187851883" MODIFIED="1562187851883"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">string </font><b>= ICON_BOOKMARK</b>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_202834778" CREATED="1562187851883" MODIFIED="1562187851883"/>
</node>
</node>
<node TEXT="." ID="ID_135842528" CREATED="1562187775259" MODIFIED="1562187776316">
<node ID="ID_263885265" CREATED="1562187851867" MODIFIED="1562187851867"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">string </font><b>= ICON_PRIO1</b>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_228411567" CREATED="1562187851867" MODIFIED="1562187851867"/>
</node>
</node>
<node TEXT="." ID="ID_1182752301" CREATED="1562187784048" MODIFIED="1562187785035">
<node ID="ID_728395196" CREATED="1562187851820" MODIFIED="1562187851851"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">string </font><b>= ICON_PRIO2</b>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_504013229" CREATED="1562187851851" MODIFIED="1562187851851"/>
</node>
</node>
<node TEXT="..." STYLE_REF="klein und grau" ID="ID_1922684157" CREATED="1562187789890" MODIFIED="1562187791430"/>
<node TEXT="." ID="ID_525589868" CREATED="1552496013370" MODIFIED="1552496014745">
<node TEXT="Mindmap" ID="ID_275483556" CREATED="1505560817042" MODIFIED="1561828757404" MIN_WIDTH="100">
<font BOLD="true"/>
<node TEXT="ATTRIBUTS of CLASS" STYLE_REF="klein und grau" ID="ID_1762944993" CREATED="1510556340486" MODIFIED="1510556383216"/>
<node TEXT="..." STYLE_REF="klein und grau" ID="ID_548643625" CREATED="1541848793712" MODIFIED="1541848794444"/>
<node TEXT="." ID="ID_1906952464" CREATED="1505562042925" MODIFIED="1505562043536">
<node FOLDED="true" ID="ID_1261149057" CREATED="1505557645742" MODIFIED="1610803716588" MIN_WIDTH="220"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">mindmap</font>&#160;<b>= </b>__init__()
    </p>
  </body>
</html>
</richcontent>
<node TEXT="FIX: use lxml module instead of xml module" STYLE_REF="ANFORDERUNG (extern)" ID="ID_1393007333" CREATED="1552641157945" MODIFIED="1552641183824">
<icon BUILTIN="yes"/>
</node>
<node TEXT="access password protected nodes" STYLE_REF="ANFORDERUNG (extern)" ID="ID_1841525373" CREATED="1552641157945" MODIFIED="1552643276469">
<icon BUILTIN="yes"/>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_27487027" CREATED="1510406557043" MODIFIED="1510577834533">
<node ID="ID_714025128" CREATED="1510406578643" MODIFIED="1510406578658"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;path&gt;</font>
  </body>
</html>
</richcontent>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_682540120" CREATED="1510555166004" MODIFIED="1510577832877">
<node ID="ID_383287030" CREATED="1510555173656" MODIFIED="1510555178669"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;type&gt;</font>
  </body>
</html>
</richcontent>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_196913558" CREATED="1510555168004" MODIFIED="1510577836025">
<node ID="ID_929653422" CREATED="1510555169700" MODIFIED="1510555178688"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;version&gt;</font>
  </body>
</html>
</richcontent>
</node>
</node>
<node TEXT="code" STYLE_REF="klein und grau" ID="ID_985363639" CREATED="1505569917734" MODIFIED="1505570192048" MIN_WIDTH="60">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1114544664" CREATED="1505569922274" MODIFIED="1505569923266">
<node TEXT="check for command line arguments" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1664024160" CREATED="1505569924460" MODIFIED="1610631162401" MIN_WIDTH="340"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1372702127" CREATED="1505569947452" MODIFIED="1505569948263">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_169392270" CREATED="1610628583128" MODIFIED="1610628583894">
<node TEXT="read out CLI and execute main command" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1306995003" CREATED="1505569952508" MODIFIED="1610631162401" MIN_WIDTH="340"/>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_452200702" CREATED="1505570157157" MODIFIED="1505570158014">
<node TEXT="update class variables" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_920434001" CREATED="1505570158016" MODIFIED="1610631162401" MIN_WIDTH="340"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_146421542" CREATED="1610628808818" MODIFIED="1610628811018">
<node TEXT="access instance variables" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_283757890" CREATED="1610628811018" MODIFIED="1610631162401" MIN_WIDTH="340"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1615598756" CREATED="1610628678801" MODIFIED="1610628681334">
<node TEXT="read mindmap in case path is given" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_489469707" CREATED="1610628681338" MODIFIED="1610631162401" MIN_WIDTH="340"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1433205417" CREATED="1610630302137" MODIFIED="1610630304075">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_526762156" CREATED="1610630304075" MODIFIED="1610630305565">
<node TEXT="determine file&apos;s map version" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_777214539" CREATED="1610630305565" MODIFIED="1610631162401" MIN_WIDTH="340">
<node TEXT="call" STYLE_REF="klein und grau" ID="ID_250339224" CREATED="1610696947430" MODIFIED="1610696949399">
<node TEXT="=ID_806082309.text" ID="ID_105517265" CREATED="1610697388795" MODIFIED="1610697530588" LINK="#ID_806082309">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_750463592" STARTINCLINATION="3098;0;" ENDINCLINATION="3098;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
<node TEXT="&gt;" STYLE_REF="klein und grau" ID="ID_1191265906" CREATED="1610697545857" MODIFIED="1610697549577">
<node ID="ID_1133498640" CREATED="1610697550091" MODIFIED="1610697561400"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;encoding&gt;</font>
  </body>
</html>
</richcontent>
</node>
</node>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1696596863" CREATED="1610630302137" MODIFIED="1610630304075">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1074107571" CREATED="1610630304075" MODIFIED="1610630305565">
<node TEXT="set parser encoding due to map version" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1825683663" CREATED="1610630305565" MODIFIED="1610631162401" MIN_WIDTH="340"/>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_811808284" CREATED="1610631125093" MODIFIED="1610631127103">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_449692471" CREATED="1610631127109" MODIFIED="1610631128597">
<node TEXT="read entire mindmap and evaluate structure" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1873575473" CREATED="1610631128597" MODIFIED="1610631162401" MIN_WIDTH="340"/>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_623084739" CREATED="1610631134326" MODIFIED="1610631169804">
<node TEXT="create mindmap if path is invalid or empty" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1241179596" CREATED="1610631169804" MODIFIED="1610631527665"/>
</node>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1454879706" CREATED="1510406618866" MODIFIED="1510406621559">
<node TEXT="=ID_335877896.text" ID="ID_38906032" CREATED="1505561337461" MODIFIED="1541683084206" LINK="#ID_335877896">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="Segoe UI" DESTINATION="ID_1832435163" STARTINCLINATION="283;0;" ENDINCLINATION="283;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_953517952" CREATED="1510556350149" MODIFIED="1510556351063">
<node FOLDED="true" ID="ID_1531153354" CREATED="1510556351063" MODIFIED="1610803716588" MIN_WIDTH="220"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">int</font>&#160;<b>= _num_of_maps</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1621996741" CREATED="1541685358656" MODIFIED="1541685358666">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="Segoe UI" DESTINATION="ID_774317224" STARTINCLINATION="528;0;" ENDINCLINATION="528;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_251753993" CREATED="1560972316153" MODIFIED="1560972321150">
<node TEXT="number of opened mindmaps" ID="ID_1056892749" CREATED="1560972322158" MODIFIED="1560972334190"/>
</node>
</node>
</node>
<node TEXT="..." STYLE_REF="klein und grau" ID="ID_1823762418" CREATED="1510557157113" MODIFIED="1541685312685"/>
<node TEXT="." ID="ID_629579095" CREATED="1505561250546" MODIFIED="1505561252096">
<node FOLDED="true" ID="ID_229642304" CREATED="1505561252098" MODIFIED="1610803716589" MIN_WIDTH="220"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">int</font>&#160;<b>= getNumOfMaps()</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="code" STYLE_REF="klein und grau" ID="ID_1284076960" CREATED="1505570179878" MODIFIED="1505570192048" MIN_WIDTH="60">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1089921327" CREATED="1510480395765" MODIFIED="1510480397342">
<node TEXT="..." ID="ID_129211598" CREATED="1510480397342" MODIFIED="1510480398576">
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_37452687" CREATED="1541685353244" MODIFIED="1541685354156">
<node TEXT="=ID_1531153354.text" ID="ID_774317224" CREATED="1541685344543" MODIFIED="1541685344585" LINK="#ID_1531153354">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_734753184" CREATED="1505561320105" MODIFIED="1505570192048" MIN_WIDTH="60">
<node TEXT="number of active map instances" ID="ID_13058313" CREATED="1510555693055" MODIFIED="1510555716785"/>
</node>
</node>
</node>
<node TEXT="." ID="ID_580489828" CREATED="1610803582530" MODIFIED="1610803583326">
<node ID="ID_1593219805" CREATED="1610803583329" MODIFIED="1610803716589" MIN_WIDTH="220"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">string </font><b>= get_new_node_id()</b>
  </body>
</html>
</richcontent>
<node TEXT="act" STYLE_REF="klein und grau" ID="ID_870790416" CREATED="1610804699921" MODIFIED="1610804699922"/>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1407180860" CREATED="1610803601291" MODIFIED="1610803601292"/>
</node>
</node>
<node TEXT="." ID="ID_655278132" CREATED="1610788339645" MODIFIED="1610788341305">
<node ID="ID_693480217" CREATED="1610788341320" MODIFIED="1610803716589" MIN_WIDTH="220"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">node </font><b>= createNode()</b>
  </body>
</html>
</richcontent>
<node TEXT="scope" STYLE_REF="klein und grau" ID="ID_1315011954" CREATED="1610790048241" MODIFIED="1610790050238">
<node TEXT="create a detached node element" ID="ID_1156546556" CREATED="1610790050271" MODIFIED="1610790056785">
<node TEXT="must be attached in order to be included within a particular mindmap" STYLE_REF="klein und grau" ID="ID_1012713252" CREATED="1610790062846" MODIFIED="1610790083450"/>
</node>
</node>
<node TEXT="code" STYLE_REF="klein und grau" ID="ID_1689260211" CREATED="1610803647522" MODIFIED="1610803648862">
<node TEXT="create and init element" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1164475979" CREATED="1610803660644" MODIFIED="1610803668171">
<node TEXT="call" STYLE_REF="klein und grau" ID="ID_825130334" CREATED="1610803650110" MODIFIED="1610803671458">
<node TEXT="=ID_1593219805.text" ID="ID_1358739800" CREATED="1610803639053" MODIFIED="1610804699922" LINK="#ID_1593219805">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_870790416" STARTINCLINATION="497;0;" ENDINCLINATION="497;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
<node TEXT="init" STYLE_REF="klein und grau" ID="ID_685967803" CREATED="1610816117621" MODIFIED="1610816119193">
<node TEXT="=ID_377364601.text" ID="ID_111848714" CREATED="1610816114001" MODIFIED="1610816144830" LINK="#ID_377364601">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1550643196" STARTINCLINATION="967;0;" ENDINCLINATION="967;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_879926999" CREATED="1505561320105" MODIFIED="1505570192048" MIN_WIDTH="60">
<node TEXT="=ID_1799662911.text" ID="ID_532277530" CREATED="1510577800693" MODIFIED="1610790115145" LINK="#ID_1799662911">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1632982554" STARTINCLINATION="1019;0;" ENDINCLINATION="1019;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
<node TEXT="DETACHED" STYLE_REF="klein und grau" ID="ID_244299792" CREATED="1610804097775" MODIFIED="1610804100677"/>
</node>
</node>
</node>
</node>
<node TEXT="..." STYLE_REF="klein und grau" ID="ID_129427893" CREATED="1510557164683" MODIFIED="1541685316424"/>
</node>
</node>
</node>
</node>
<node TEXT="[ cls ]" STYLE_REF="klein und grau" ID="ID_654460877" CREATED="1510395207413" MODIFIED="1583832904160" MIN_WIDTH="60">
<node ID="ID_1554808123" CREATED="1505561362709" MODIFIED="1610814787155" MIN_WIDTH="120">
<icon BUILTIN="list"/>
<richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">Mindmap</font>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="scope" STYLE_REF="klein und grau" ID="ID_234724023" CREATED="1505561359214" MODIFIED="1505561361361">
<node TEXT="general mindmap object" ID="ID_335877896" CREATED="1505561322915" MODIFIED="1552495853698">
<node TEXT="act" STYLE_REF="klein und grau" ID="ID_1832435163" CREATED="1541683084206" MODIFIED="1541683084206"/>
</node>
</node>
<node TEXT="..." STYLE_REF="klein und grau" ID="ID_284451710" CREATED="1541848818702" MODIFIED="1541848819874"/>
<node TEXT="." ID="ID_376155927" CREATED="1510556263187" MODIFIED="1510556263571">
<node FOLDED="true" ID="ID_158319178" CREATED="1544166545280" MODIFIED="1610789962684" MIN_WIDTH="300"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">string </font><b>= _path</b>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_286678451" CREATED="1544166545284" MODIFIED="1544166545286">
<node TEXT="path to mindmap file of instance" ID="ID_289556126" CREATED="1544166546988" MODIFIED="1544166564343"/>
</node>
</node>
</node>
<node TEXT="." ID="ID_1326283821" CREATED="1510556264643" MODIFIED="1510556265543">
<node FOLDED="true" ID="ID_1694516548" CREATED="1560970167632" MODIFIED="1610789962684" MIN_WIDTH="300"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">string </font><b>= _type</b>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_24502524" CREATED="1560970167632" MODIFIED="1560970167632">
<node TEXT="tape string" ID="ID_731272568" CREATED="1560970170337" MODIFIED="1560970176160"/>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1009672412" CREATED="1560970176601" MODIFIED="1560970178487">
<node TEXT="freeplane" ID="ID_1788507628" CREATED="1560970178487" MODIFIED="1560970181509">
<font BOLD="true"/>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1139858676" CREATED="1560970182919" MODIFIED="1560970184693">
<node TEXT="freemind" ID="ID_751647261" CREATED="1560970184693" MODIFIED="1560970187875">
<font BOLD="true"/>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1728312369" CREATED="1560970188694" MODIFIED="1560970190190">
<node TEXT="..." ID="ID_494055724" CREATED="1560970190190" MODIFIED="1560970191007"/>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_1814494217" CREATED="1510556266515" MODIFIED="1510556266889">
<node FOLDED="true" ID="ID_883264090" CREATED="1544166545233" MODIFIED="1610789962684" MIN_WIDTH="300"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">string </font><b>= _version</b>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1361111386" CREATED="1544166545245" MODIFIED="1544166545251">
<node TEXT="version string of mindmap" ID="ID_1482087579" CREATED="1544166566588" MODIFIED="1544166577222"/>
</node>
</node>
</node>
<node TEXT="." ID="ID_144406957" CREATED="1510556268179" MODIFIED="1510556269088">
<node FOLDED="true" ID="ID_610692546" CREATED="1560970386837" MODIFIED="1610789962685" MIN_WIDTH="300"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">lxml_etree </font><b>= _mindmap</b>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_632018160" CREATED="1560970386853" MODIFIED="1560970386853">
<node TEXT="element tree object representing entire mindmap" ID="ID_487975659" CREATED="1560970388714" MODIFIED="1560970435798" LINK="file:/I:/Documents/mindmaps/language__Python.mm#ID_1080473260"/>
</node>
</node>
</node>
<node TEXT="." ID="ID_316259014" CREATED="1560970508671" MODIFIED="1560970509505">
<node FOLDED="true" ID="ID_1438826838" CREATED="1560970530796" MODIFIED="1610789962685" MIN_WIDTH="300"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">lxml_etree </font><b>= _root</b>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_321415384" CREATED="1561911268196" MODIFIED="1561911268196">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1825245022" STARTINCLINATION="619;0;" ENDINCLINATION="619;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_475655491" CREATED="1560970530811" MODIFIED="1560970530811">
<node TEXT="element tree object representing entire mindmap" ID="ID_1121586084" CREATED="1560970388714" MODIFIED="1560970435798" LINK="file:/I:/Documents/mindmaps/language__Python.mm#ID_1080473260"/>
</node>
</node>
</node>
<node TEXT="." ID="ID_184888357" CREATED="1510556270083" MODIFIED="1510556270494">
<node ID="ID_306486355" CREATED="1544166513570" MODIFIED="1610789962685" MIN_WIDTH="300"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">lxml_etree </font><b>= _rootnode</b>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_978516134" CREATED="1544166513577" MODIFIED="1544166513581">
<node TEXT="element tree object representing the first (central) Freeplane node" ID="ID_494780598" CREATED="1560970388714" MODIFIED="1610909146337" LINK="file:/I:/Documents/mindmaps/language__Python.mm#ID_1080473260"/>
</node>
</node>
</node>
<node TEXT="." ID="ID_1270589654" CREATED="1541683111335" MODIFIED="1541683112214">
<node ID="ID_1125959904" CREATED="1544166501407" MODIFIED="1610789962685" MIN_WIDTH="300"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">dict </font><b>= _parentmap{}</b>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1053325215" CREATED="1610814953465" MODIFIED="1610817366350">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_983098355" STARTINCLINATION="182;0;" ENDINCLINATION="182;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1588262998" STARTINCLINATION="1026;0;" ENDINCLINATION="1026;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
<node TEXT="act" STYLE_REF="klein und grau" ID="ID_265888356" CREATED="1592223176815" MODIFIED="1592223176815"/>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_141703536" CREATED="1544166501416" MODIFIED="1544166501419">
<node TEXT="dict of" ID="ID_1758336909" CREATED="1544166474701" MODIFIED="1544166477030">
<node ID="ID_1844674618" CREATED="1541683151087" MODIFIED="1541683151097"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;node&gt;</font><b>:</b><font color="#0000ff">&lt;pnode&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="&lt;node&gt;" STYLE_REF="klein und grau" ID="ID_967839787" CREATED="1541683151097" MODIFIED="1541683190788" MIN_WIDTH="80">
<node TEXT="node object reference of ElementTree module" ID="ID_1001364632" CREATED="1517378570970" MODIFIED="1561900016195"/>
</node>
<node TEXT="&lt;pnode&gt;" STYLE_REF="klein und grau" ID="ID_77786357" CREATED="1541683151107" MODIFIED="1541683190788" MIN_WIDTH="80">
<node TEXT="node&apos;s parent node object reference of ElementTree module" ID="ID_646037154" CREATED="1541683182346" MODIFIED="1561900024212"/>
</node>
</node>
</node>
</node>
</node>
</node>
<node TEXT="..." STYLE_REF="klein und grau" ID="ID_1005081206" CREATED="1541685292241" MODIFIED="1541685293593"/>
<node TEXT="." ID="ID_1667957606" CREATED="1610690979723" MODIFIED="1610690980768">
<node FOLDED="true" ID="ID_1366356904" CREATED="1610690980771" MODIFIED="1610789962685" MIN_WIDTH="300"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">dict </font><b>= Styles</b>
  </body>
</html>
</richcontent>
<node TEXT="sets / returns" STYLE_REF="klein und grau" ID="ID_46713874" CREATED="1610691039972" MODIFIED="1610691039976">
<node TEXT="dict of" ID="ID_1384913304" CREATED="1610691877977" MODIFIED="1610691880564">
<node TEXT="user-defined style" ID="ID_858714271" CREATED="1610691880565" MODIFIED="1610691886747"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_70442752" CREATED="1610691909679" MODIFIED="1610691912824">
<node ID="ID_414283837" CREATED="1610691912830" MODIFIED="1610692111315"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <b>{ &quot;</b><font color="#0000ff">&lt;stylename&gt;</font><b>&quot;: { &quot;</b><font color="#0000ff">&lt;key&gt;</font><b>&quot;: &quot;</b><font color="#0000ff">&lt;value&gt;</font><b>&quot; } </b><font color="#0000ff">[</font><b> , </b><font color="#0000ff">]</font><b> </b><font color="#0000ff">]+</font><b> }</b>
  </body>
</html>
</richcontent>
<node TEXT="&lt;stylename&gt;" STYLE_REF="klein und grau" ID="ID_810145815" CREATED="1610692111318" MODIFIED="1610692111321">
<node TEXT="name of user-defined style" ID="ID_180520672" CREATED="1610692116291" MODIFIED="1610692122841">
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_821781886" CREATED="1610692124318" MODIFIED="1610692124322">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1667751251" STARTINCLINATION="195;0;" ENDINCLINATION="195;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="&lt;key&gt;" STYLE_REF="klein und grau" ID="ID_1959234281" CREATED="1610692111322" MODIFIED="1610692111322">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_68491775" CREATED="1610694772421" MODIFIED="1610694772426">
<node TEXT="color" ID="ID_1687353322" CREATED="1610692233245" MODIFIED="1610694794175" MIN_WIDTH="100">
<font BOLD="true"/>
<node TEXT="&lt;value&gt;" STYLE_REF="klein und grau" ID="ID_112864890" CREATED="1610692383884" MODIFIED="1610692386703">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_277505903" CREATED="1610694788262" MODIFIED="1610694788263">
<node TEXT="#999999" ID="ID_1461730219" CREATED="1610692388733" MODIFIED="1610692396376"/>
</node>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_731044886" CREATED="1610694772438" MODIFIED="1610694772439">
<node TEXT="bgcolor" ID="ID_1320506705" CREATED="1610692242507" MODIFIED="1610694794175" MIN_WIDTH="100">
<font BOLD="true"/>
<node TEXT="&lt;value&gt;" STYLE_REF="klein und grau" ID="ID_1261107135" CREATED="1610692383884" MODIFIED="1610692386703">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1455429741" CREATED="1610694786368" MODIFIED="1610694786369">
<node TEXT="#111111" ID="ID_1510559963" CREATED="1610692388733" MODIFIED="1610692406502"/>
</node>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1633763384" CREATED="1610694772447" MODIFIED="1610694772449">
<node TEXT="fontname" ID="ID_773262144" CREATED="1610692258570" MODIFIED="1610726630237" MIN_WIDTH="100">
<font BOLD="true"/>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_673024040" CREATED="1610694772454" MODIFIED="1610694772456">
<node TEXT="fontsize" ID="ID_458294124" CREATED="1610692263798" MODIFIED="1610726630238" MIN_WIDTH="100">
<font BOLD="true"/>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1931607555" CREATED="1610694772465" MODIFIED="1610694772466">
<node TEXT="icons" STYLE_REF="ANFORDERUNG (extern)" ID="ID_1863427737" CREATED="1610692277522" MODIFIED="1610694794176" MIN_WIDTH="100"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1037180957" CREATED="1610694772474" MODIFIED="1610694772475">
<node TEXT="edgestyle" STYLE_REF="ANFORDERUNG (extern)" ID="ID_52875567" CREATED="1610692301974" MODIFIED="1610694794176" MIN_WIDTH="100"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_63813156" CREATED="1610694772482" MODIFIED="1610694772484">
<node TEXT="cloudcolor" STYLE_REF="ANFORDERUNG (extern)" ID="ID_1180378244" CREATED="1610692305259" MODIFIED="1610694794176" MIN_WIDTH="100"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_861408221" CREATED="1610694772489" MODIFIED="1610694772491">
<node TEXT="boldfont" STYLE_REF="ANFORDERUNG (extern)" ID="ID_1646048579" CREATED="1610692321229" MODIFIED="1610694794176" MIN_WIDTH="100"/>
</node>
</node>
<node TEXT="&lt;value&gt;" STYLE_REF="klein und grau" ID="ID_752321631" CREATED="1610692111323" MODIFIED="1610692111324"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_155224387" CREATED="1610726655411" MODIFIED="1610726656911">
<node ID="ID_1717135216" CREATED="1610726656914" MODIFIED="1610789962685" MIN_WIDTH="300"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">bool </font><b>= addStyle()</b>
  </body>
</html>
</richcontent>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_971448652" CREATED="1610726672417" MODIFIED="1610726674577">
<node TEXT="name" ID="ID_1040142558" CREATED="1610726676187" MODIFIED="1610726683263"/>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_834940980" CREATED="1610726683994" MODIFIED="1610726686156">
<node TEXT="settings" ID="ID_200535220" CREATED="1610726686175" MODIFIED="1610726701326">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1947164389" CREATED="1610727832742" MODIFIED="1610727837869">
<node ID="ID_1665904969" CREATED="1610727837871" MODIFIED="1610727911510"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <b>{ '</b><font color="#0000ff">&lt;key&gt;</font><b>': '</b><font color="#0000ff">&lt;value&gt;</font><b>' </b><font color="#0000ff">[</font><b> , '</b><font color="#0000ff">&lt;key&gt;</font><b>': '</b><font color="#0000ff">&lt;value&gt;</font><b>' </b><font color="#0000ff">]</font><b> }</b>
  </body>
</html>
</richcontent>
<node TEXT="&lt;key&gt;" STYLE_REF="klein und grau" ID="ID_1112705161" CREATED="1610727911514" MODIFIED="1610727917204" LINK="#ID_1959234281"/>
<node TEXT="&lt;value&gt;" STYLE_REF="klein und grau" ID="ID_6004946" CREATED="1610727911517" MODIFIED="1610727923272" LINK="#ID_752321631"/>
</node>
</node>
</node>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_471539148" CREATED="1610726670358" MODIFIED="1610726670364"/>
</node>
</node>
<node TEXT="." ID="ID_1252217607" CREATED="1505561250546" MODIFIED="1505561252096">
<node ID="ID_1566504926" CREATED="1505561252098" MODIFIED="1610789962685" MIN_WIDTH="300"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">node</font>&#160;<b>= RootNode</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="scope" STYLE_REF="klein und grau" ID="ID_420270474" CREATED="1610784747579" MODIFIED="1610784749728">
<node TEXT="first Freeplane node below map element" ID="ID_959645613" CREATED="1610784749741" MODIFIED="1610784778008"/>
</node>
<node TEXT="code" STYLE_REF="klein und grau" ID="ID_1177582135" CREATED="1505570179878" MODIFIED="1505570192048" MIN_WIDTH="60">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1061273255" CREATED="1510480395765" MODIFIED="1510480397342">
<node TEXT="..." ID="ID_1106464533" CREATED="1510480397342" MODIFIED="1510480398576"/>
</node>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1308401743" CREATED="1505561320105" MODIFIED="1505570192048" MIN_WIDTH="60">
<node TEXT="=ID_1799662911.text" ID="ID_1576006193" CREATED="1510577800693" MODIFIED="1610817374041" LINK="#ID_1799662911">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1632982554" STARTINCLINATION="459;0;" ENDINCLINATION="459;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_1390136885" CREATED="1505561368013" MODIFIED="1505561368676">
<node ID="ID_64479114" CREATED="1505561368678" MODIFIED="1610789962685" MIN_WIDTH="300"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">list</font>&#160;<b>= findNodes()</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="code" STYLE_REF="klein und grau" ID="ID_1014195270" CREATED="1541696381321" MODIFIED="1561910593507">
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_908288157" CREATED="1510579710601" MODIFIED="1561885931914">
<node ID="ID_158763597" CREATED="1510579713078" MODIFIED="1561885956040" MIN_WIDTH="100"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;id&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_346473125" CREATED="1561911386576" MODIFIED="1561911386580">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1748082658" STARTINCLINATION="307;0;" ENDINCLINATION="307;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_1264861879" CREATED="1510651439185" MODIFIED="1561885932760">
<node ID="ID_1195825663" CREATED="1510651445412" MODIFIED="1561885956040" MIN_WIDTH="100"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;core&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_382868423" CREATED="1561911386583" MODIFIED="1561911386583">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_321164648" STARTINCLINATION="316;0;" ENDINCLINATION="316;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_1475720508" CREATED="1510651541460" MODIFIED="1561885933330">
<node ID="ID_918311773" CREATED="1510651471610" MODIFIED="1561885956040" MIN_WIDTH="100"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;attrib&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1646975466" CREATED="1561911386599" MODIFIED="1561911386599">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_755080415" STARTINCLINATION="319;0;" ENDINCLINATION="319;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_946293272" CREATED="1510651543602" MODIFIED="1561885933813">
<node ID="ID_1324050013" CREATED="1510651475698" MODIFIED="1561885956040" MIN_WIDTH="100"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;details&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1784976760" CREATED="1561911386615" MODIFIED="1561911386615">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_977562200" STARTINCLINATION="322;0;" ENDINCLINATION="322;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_1237481541" CREATED="1510651546065" MODIFIED="1561885934245">
<node ID="ID_1150269385" CREATED="1510651480080" MODIFIED="1561885956040" MIN_WIDTH="100"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;notes&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_993867653" CREATED="1561911386631" MODIFIED="1561911386631">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_581702460" STARTINCLINATION="316;0;" ENDINCLINATION="316;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_530255767" CREATED="1510651548455" MODIFIED="1561885934730">
<node ID="ID_1217632414" CREATED="1510651485793" MODIFIED="1561885956040" MIN_WIDTH="100"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;link&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_505203506" CREATED="1561911386631" MODIFIED="1561911386646">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_567398606" STARTINCLINATION="307;0;" ENDINCLINATION="307;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_936836106" CREATED="1561885936948" MODIFIED="1561885939149">
<node ID="ID_821404078" CREATED="1561885939149" MODIFIED="1561885956040" MIN_WIDTH="100"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;icon&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1951658776" CREATED="1561911386646" MODIFIED="1561911386646">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_578427820" STARTINCLINATION="308;0;" ENDINCLINATION="308;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_1927450169" CREATED="1510651550294" MODIFIED="1561885935883">
<node ID="ID_566215241" CREATED="1510651487750" MODIFIED="1561885956056" MIN_WIDTH="100"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;bExact&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1422548899" CREATED="1561911386662" MODIFIED="1561911386662">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_894311227" STARTINCLINATION="316;0;" ENDINCLINATION="316;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_911429878" CREATED="1561911218133" MODIFIED="1561911219486">
<node TEXT="find list of nodes in map" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_349240384" CREATED="1561911219486" MODIFIED="1561911289676" MIN_WIDTH="200">
<node TEXT="&lt;&lt;" STYLE_REF="klein und grau" ID="ID_1754407161" CREATED="1561911260072" MODIFIED="1561911264072">
<node TEXT="=ID_1438826838.text" ID="ID_1825245022" CREATED="1561911254147" MODIFIED="1561911254264" LINK="#ID_1438826838">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_350179275" CREATED="1561911367516" MODIFIED="1561911368405">
<node TEXT="=ID_158763597.text" ID="ID_1748082658" CREATED="1561911325941" MODIFIED="1561911326120" LINK="#ID_158763597">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_897795743" CREATED="1561911364717" MODIFIED="1561911365686">
<node TEXT="=ID_1195825663.text" ID="ID_321164648" CREATED="1561911326120" MODIFIED="1561911326204" LINK="#ID_1195825663">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_1104643852" CREATED="1561911362510" MODIFIED="1561911363369">
<node TEXT="=ID_918311773.text" ID="ID_755080415" CREATED="1561911326204" MODIFIED="1561911326305" LINK="#ID_918311773">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_60732827" CREATED="1561911360270" MODIFIED="1561911361096">
<node TEXT="=ID_1324050013.text" ID="ID_977562200" CREATED="1561911326305" MODIFIED="1561911326389" LINK="#ID_1324050013">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_917901663" CREATED="1561911356909" MODIFIED="1561911358563">
<node TEXT="=ID_1150269385.text" ID="ID_581702460" CREATED="1561911326389" MODIFIED="1561911326474" LINK="#ID_1150269385">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_682648057" CREATED="1561911354640" MODIFIED="1561911355608">
<node TEXT="=ID_1217632414.text" ID="ID_567398606" CREATED="1561911326474" MODIFIED="1561911326559" LINK="#ID_1217632414">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_1205893773" CREATED="1561911352243" MODIFIED="1561911353187">
<node TEXT="=ID_821404078.text" ID="ID_578427820" CREATED="1561911326559" MODIFIED="1561911326643" LINK="#ID_821404078">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_1421258245" CREATED="1561911347533" MODIFIED="1561911349987">
<node TEXT="=ID_566215241.text" ID="ID_894311227" CREATED="1561911326643" MODIFIED="1561911326743" LINK="#ID_566215241">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="call" STYLE_REF="klein und grau" ID="ID_931839984" CREATED="1561911229221" MODIFIED="1561911239692">
<node TEXT="=ID_838144026.text" ID="ID_1151280308" CREATED="1561911190261" MODIFIED="1561911677046" LINK="#ID_838144026">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_330698355" STARTINCLINATION="2497;0;" ENDINCLINATION="2497;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
<node TEXT="&gt;" STYLE_REF="klein und grau" ID="ID_1377034906" CREATED="1561911300786" MODIFIED="1561911303090">
<node ID="ID_296536495" CREATED="1561911303090" MODIFIED="1561911307030"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;lstNodes&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1914028478" CREATED="1561911307507" MODIFIED="1561911307507">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_338495438" STARTINCLINATION="90;0;" ENDINCLINATION="90;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1916680512" CREATED="1561910604322" MODIFIED="1561910607073">
<node TEXT="create Node instances" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_524212884" CREATED="1561910607073" MODIFIED="1561911289676" MIN_WIDTH="200">
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_1972201095" CREATED="1561911311922" MODIFIED="1561911312832">
<node TEXT="=ID_296536495.text" ID="ID_338495438" CREATED="1561911307421" MODIFIED="1561911307545" LINK="#ID_296536495">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="init" STYLE_REF="klein und grau" ID="ID_1582032106" CREATED="1561910610359" MODIFIED="1561910613408">
<node TEXT="=ID_645829533.text" ID="ID_120276278" CREATED="1561910559145" MODIFIED="1561910572296" LINK="#ID_645829533">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1508706568" STARTINCLINATION="1160;0;" ENDINCLINATION="1160;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1177812346" CREATED="1510577789654" MODIFIED="1510577795846">
<node TEXT="list of" ID="ID_1916614685" CREATED="1510606395792" MODIFIED="1561885962093">
<node TEXT="=ID_1799662911.text" ID="ID_730977165" CREATED="1510577800693" MODIFIED="1561910876681" LINK="#ID_1799662911">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1632982554" STARTINCLINATION="329;0;" ENDINCLINATION="329;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="..." STYLE_REF="klein und grau" ID="ID_1646806933" CREATED="1510399680602" MODIFIED="1541685445716"/>
<node TEXT="." ID="ID_327192714" CREATED="1561885989041" MODIFIED="1561885990785">
<node FOLDED="true" ID="ID_1193249584" CREATED="1561886009649" MODIFIED="1610814815452" MIN_WIDTH="300"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">None</font><b>&#160;= save( </b><font color="#0000ff">&lt;path&gt;</font><b>&#160;</b><font color="#0000ff">[</font><b>&#160;, </b><font color="#0000ff">&lt;encoding&gt; ]</font><b>&#160;)</b>
  </body>
</html>
</richcontent>
<node TEXT="&lt;path&gt;" STYLE_REF="klein und grau" ID="ID_1194446480" CREATED="1561886009649" MODIFIED="1610697817886" MIN_WIDTH="100">
<node TEXT="file path where to put mindmap" ID="ID_760900144" CREATED="1561892469077" MODIFIED="1610697859696" MIN_WIDTH="240">
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1979949577" CREATED="1610697862297" MODIFIED="1610697862298">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_311923547" STARTINCLINATION="377;0;" ENDINCLINATION="377;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="&lt;encoding&gt;" STYLE_REF="klein und grau" ID="ID_251893933" CREATED="1610697760882" MODIFIED="1610697817886" MIN_WIDTH="100">
<node TEXT="encoding" ID="ID_1128466882" CREATED="1610697767743" MODIFIED="1610697859696" MIN_WIDTH="240">
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1707664041" CREATED="1610697862287" MODIFIED="1610697862291">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1765126029" STARTINCLINATION="182;0;" ENDINCLINATION="182;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="code" STYLE_REF="klein und grau" ID="ID_1586805597" CREATED="1610697496700" MODIFIED="1610697817888" MIN_WIDTH="100">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1074957895" CREATED="1610697493954" MODIFIED="1610697493957">
<node TEXT="auto-determine and set encoding" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_33091168" CREATED="1610697450574" MODIFIED="1610723030928" MIN_WIDTH="280">
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_1703333130" CREATED="1610697796783" MODIFIED="1610697797750">
<node TEXT="=ID_1128466882.text" ID="ID_1765126029" CREATED="1610697792126" MODIFIED="1610697792143" LINK="#ID_1128466882">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="call" STYLE_REF="klein und grau" ID="ID_562348900" CREATED="1610697438691" MODIFIED="1610697440170">
<node TEXT="=ID_806082309.text" ID="ID_8421139" CREATED="1610697423736" MODIFIED="1610697530600" LINK="#ID_806082309">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_750463592" STARTINCLINATION="2100;0;" ENDINCLINATION="2100;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
<node TEXT="&gt;" STYLE_REF="klein und grau" ID="ID_1266381441" CREATED="1610697545857" MODIFIED="1610697549577">
<node ID="ID_1195165599" CREATED="1610697550091" MODIFIED="1610697561400"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;encoding&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_127551613" CREATED="1610697583050" MODIFIED="1610697583052">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_805355773" STARTINCLINATION="95;0;" ENDINCLINATION="95;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1167208048" CREATED="1610722979082" MODIFIED="1610722980688">
<node TEXT="create XML formatted output string" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_185367528" CREATED="1610722980690" MODIFIED="1610723030929" MIN_WIDTH="280"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_860592974" CREATED="1610722996324" MODIFIED="1610722998423">
<node TEXT="sanitize string content" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_841019483" CREATED="1610722998427" MODIFIED="1610723030930" MIN_WIDTH="280"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_520638300" CREATED="1610697493962" MODIFIED="1610697493963">
<node TEXT="write content into file" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1632534438" CREATED="1610697482087" MODIFIED="1610723030931" MIN_WIDTH="280">
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_987523579" CREATED="1610697586696" MODIFIED="1610697588442">
<node TEXT="=ID_1195165599.text" ID="ID_805355773" CREATED="1610697583035" MODIFIED="1610697583058" LINK="#ID_1195165599">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_1482087085" CREATED="1610697845793" MODIFIED="1610697846875">
<node TEXT="=ID_760900144.text" ID="ID_311923547" CREATED="1610697840838" MODIFIED="1610697840858" LINK="#ID_760900144">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&gt;&gt;" STYLE_REF="klein und grau" ID="ID_1142342254" CREATED="1610697594315" MODIFIED="1610697596712"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_413994062" CREATED="1610789934528" MODIFIED="1610789935401">
<node ID="ID_1875186589" CREATED="1610789935407" MODIFIED="1610789962686" MIN_WIDTH="300"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">None </font><b>= test()</b>
  </body>
</html>
</richcontent>
</node>
</node>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_417085788" CREATED="1610873586570" MODIFIED="1610873586570">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1379150542" STARTINCLINATION="75;0;" ENDINCLINATION="75;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
<node ID="ID_377364601" CREATED="1610814724161" MODIFIED="1610814787155" MIN_WIDTH="120"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">Branch</font>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="act" STYLE_REF="klein und grau" ID="ID_1550643196" CREATED="1610816144829" MODIFIED="1610816144830"/>
<node TEXT="scope" STYLE_REF="klein und grau" ID="ID_218883297" CREATED="1610814731157" MODIFIED="1610814733376">
<node TEXT="branch node object" ID="ID_1162766946" CREATED="1610814733841" MODIFIED="1610814740251">
<node TEXT="act" STYLE_REF="klein und grau" ID="ID_1811713131" CREATED="1610815546362" MODIFIED="1610815546363"/>
<node TEXT="as head of detached partial tree" STYLE_REF="klein und grau" ID="ID_1153822500" CREATED="1610814740253" MODIFIED="1610814752773"/>
</node>
</node>
<node TEXT="." ID="ID_1806767923" CREATED="1610873000941" MODIFIED="1610873003265">
<node ID="ID_319634852" CREATED="1610873003265" MODIFIED="1610873039912" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">map </font><b>= _map</b>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_182354321" CREATED="1610874026462" MODIFIED="1610874026462">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_605939720" STARTINCLINATION="1254;0;" ENDINCLINATION="1254;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
<node TEXT="act" STYLE_REF="klein und grau" ID="ID_740997091" CREATED="1610874025370" MODIFIED="1610874025370"/>
<node TEXT="scope" STYLE_REF="klein und grau" ID="ID_1960843049" CREATED="1610873044438" MODIFIED="1610873053816">
<node TEXT="initially &quot;None&quot;, but set to valid entry as soon as branch gets attached to mindmap" ID="ID_58343616" CREATED="1610873055072" MODIFIED="1610873088900"/>
</node>
<node TEXT="sets / returns" STYLE_REF="klein und grau" ID="ID_1572018931" CREATED="1610873022705" MODIFIED="1610873022705"/>
</node>
</node>
<node TEXT="." ID="ID_493292435" CREATED="1610814788510" MODIFIED="1610814789619">
<node ID="ID_1376915101" CREATED="1610814789621" MODIFIED="1610873039912" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">dict </font><b>= _parentmap{}</b>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_182703996" CREATED="1610818440533" MODIFIED="1610818440534">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1062094229" STARTINCLINATION="1135;0;" ENDINCLINATION="1135;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_831444030" STARTINCLINATION="688;0;" ENDINCLINATION="688;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
<node TEXT="act" STYLE_REF="klein und grau" ID="ID_294932515" CREATED="1610818439902" MODIFIED="1610818439905"/>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_701818507" CREATED="1544166501416" MODIFIED="1544166501419">
<node TEXT="dict of" ID="ID_203457438" CREATED="1544166474701" MODIFIED="1544166477030">
<node ID="ID_355117341" CREATED="1541683151087" MODIFIED="1541683151097"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;node&gt;</font><b>:</b><font color="#0000ff">&lt;pnode&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="&lt;node&gt;" STYLE_REF="klein und grau" ID="ID_263106279" CREATED="1541683151097" MODIFIED="1541683190788" MIN_WIDTH="80">
<node TEXT="node object reference of ElementTree module" ID="ID_1963194914" CREATED="1517378570970" MODIFIED="1561900016195"/>
</node>
<node TEXT="&lt;pnode&gt;" STYLE_REF="klein und grau" ID="ID_255246060" CREATED="1541683151107" MODIFIED="1541683190788" MIN_WIDTH="80">
<node TEXT="node&apos;s parent node object reference of ElementTree module" ID="ID_1076999413" CREATED="1541683182346" MODIFIED="1561900024212"/>
</node>
</node>
</node>
</node>
</node>
</node>
</node>
<node ID="ID_645829533" CREATED="1505560852961" MODIFIED="1611166442103" MIN_WIDTH="120">
<icon BUILTIN="list"/>
<richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">Node</font>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_767913220" CREATED="1610873969249" MODIFIED="1610873969267">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1024840865" STARTINCLINATION="1149;0;" ENDINCLINATION="1149;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
<node TEXT="act" STYLE_REF="klein und grau" ID="ID_1508706568" CREATED="1561910572294" MODIFIED="1561910572296"/>
<node TEXT="scope" STYLE_REF="klein und grau" ID="ID_837722073" CREATED="1505560859560" MODIFIED="1505560861036">
<node TEXT="node object of mindmap" ID="ID_1799662911" CREATED="1505560861728" MODIFIED="1505560868189">
<node TEXT="act" STYLE_REF="klein und grau" ID="ID_1632982554" CREATED="1561910876607" MODIFIED="1561910876607"/>
</node>
</node>
<node TEXT="..." STYLE_REF="klein und grau" ID="ID_892838308" CREATED="1541843390705" MODIFIED="1541843391636"/>
<node TEXT="." ID="ID_1897266944" CREATED="1510654746821" MODIFIED="1510654748729">
<node TEXT="__init__()" FOLDED="true" ID="ID_1942601393" CREATED="1510654748729" MODIFIED="1611154006600" MIN_WIDTH="320">
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_1991091169" CREATED="1541683628921" MODIFIED="1541683630690">
<node ID="ID_436041325" CREATED="1541683630692" MODIFIED="1541683658722"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;node&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_989158021" CREATED="1561899340614" MODIFIED="1561899340617">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1565451509" STARTINCLINATION="187;0;" ENDINCLINATION="187;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
<node TEXT="ElementTree node" STYLE_REF="klein und grau" ID="ID_358300472" CREATED="1541683659940" MODIFIED="1541683667152"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_1399128639" CREATED="1541696133478" MODIFIED="1541696134808">
<node ID="ID_1507403031" CREATED="1541696134810" MODIFIED="1541696140390"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">&lt;Map&gt;</font>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1537114876" CREATED="1561899340588" MODIFIED="1561899340588">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1045587397" STARTINCLINATION="188;0;" ENDINCLINATION="188;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
<node TEXT="Map reference" STYLE_REF="klein und grau" ID="ID_950008186" CREATED="1541696141348" MODIFIED="1541696154170"/>
</node>
</node>
<node TEXT="code" STYLE_REF="klein und grau" ID="ID_103347357" CREATED="1610804662265" MODIFIED="1610804663580">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_424229725" CREATED="1510939344504" MODIFIED="1510939348793">
<node TEXT="initialize instance" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1347351281" CREATED="1510939348794" MODIFIED="1610804676375" MIN_WIDTH="240">
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_1803214297" CREATED="1561899331287" MODIFIED="1561899332574">
<node TEXT="=ID_436041325.text" ID="ID_1565451509" CREATED="1561899324610" MODIFIED="1561899324688" LINK="#ID_436041325">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&gt;&gt;" STYLE_REF="klein und grau" ID="ID_943094421" CREATED="1522250322703" MODIFIED="1561899310716">
<node TEXT="=ID_705056167.text" ID="ID_594862448" CREATED="1522250334421" MODIFIED="1561899370098" LINK="#ID_705056167">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_256259891" STARTINCLINATION="380;0;" ENDINCLINATION="380;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_350034745" CREATED="1561899334324" MODIFIED="1561899335491">
<node TEXT="=ID_1507403031.text" ID="ID_1045587397" CREATED="1561899324429" MODIFIED="1561899324610" LINK="#ID_1507403031">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&gt;&gt;" STYLE_REF="klein und grau" ID="ID_639126021" CREATED="1522250346174" MODIFIED="1561899307878">
<node TEXT="=ID_1257855042.text" ID="ID_889818304" CREATED="1561899284925" MODIFIED="1561899347104" LINK="#ID_1257855042">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1554020873" STARTINCLINATION="356;0;" ENDINCLINATION="356;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1181782749" CREATED="1610804664314" MODIFIED="1610804665913">
<node TEXT="create unique session node id" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_37389734" CREATED="1610804665924" MODIFIED="1610804676375" MIN_WIDTH="240">
<node TEXT="call" STYLE_REF="klein und grau" ID="ID_439206260" CREATED="1610803650110" MODIFIED="1610803671458">
<node TEXT="=ID_1593219805.text" ID="ID_999377099" CREATED="1610803639053" MODIFIED="1610804699933" LINK="#ID_1593219805">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_870790416" STARTINCLINATION="1135;0;" ENDINCLINATION="1135;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_1010558939" CREATED="1505561972624" MODIFIED="1505561973375">
<node FOLDED="true" ID="ID_705056167" CREATED="1510557134618" MODIFIED="1611154006602" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">lxml_etree </font><b>= _node</b>
  </body>
</html>
</richcontent>
<node TEXT="act" STYLE_REF="klein und grau" ID="ID_256259891" CREATED="1561899370098" MODIFIED="1561899370098"/>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_280626303" CREATED="1561899366954" MODIFIED="1561899366954">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1533823349" STARTINCLINATION="708;0;" ENDINCLINATION="708;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1806474674" CREATED="1510557134634" MODIFIED="1510557134634">
<node TEXT="element tree object representing entire mindmap" ID="ID_365790165" CREATED="1560970388714" MODIFIED="1560970435798" LINK="file:/I:/Documents/mindmaps/language__Python.mm#ID_1080473260"/>
</node>
</node>
</node>
<node TEXT="." ID="ID_1610990854" CREATED="1541682988494" MODIFIED="1541682990624">
<node ID="ID_1257855042" CREATED="1541683002386" MODIFIED="1611154006602" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">map </font><b>= _map</b>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_54055486" CREATED="1561910863339" MODIFIED="1561910863339">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_953738819" STARTINCLINATION="1092;0;" ENDINCLINATION="1092;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_306460805" STARTINCLINATION="836;0;" ENDINCLINATION="836;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
<node TEXT="act" STYLE_REF="klein und grau" ID="ID_1554020873" CREATED="1561899347104" MODIFIED="1561899347104"/>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_912555562" CREATED="1541683002396" MODIFIED="1541683002396">
<node TEXT="=ID_335877896.text" ID="ID_1985302922" CREATED="1541683024275" MODIFIED="1541683084226" LINK="#ID_335877896">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="Segoe UI" DESTINATION="ID_1832435163" STARTINCLINATION="445;0;" ENDINCLINATION="445;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
<node TEXT="the map this node is associated with" STYLE_REF="klein und grau" ID="ID_272949561" CREATED="1541843718375" MODIFIED="1541843730637"/>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_1581584487" CREATED="1610814580614" MODIFIED="1610814581526">
<node ID="ID_1984205011" CREATED="1610814581533" MODIFIED="1611154006603" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">branch </font><b>= _branch</b>
  </body>
</html>
</richcontent>
<node TEXT="scope" STYLE_REF="klein und grau" ID="ID_633180063" CREATED="1610814669417" MODIFIED="1610814673049">
<node TEXT="temporary head of tree" ID="ID_1002559355" CREATED="1610814673098" MODIFIED="1610814713144">
<node TEXT="as long as respective nodes are detached" STYLE_REF="klein und grau" ID="ID_433998175" CREATED="1610814713667" MODIFIED="1610814715062"/>
</node>
</node>
<node TEXT="sets / returns" STYLE_REF="klein und grau" ID="ID_1432859329" CREATED="1610814769420" MODIFIED="1610814769421">
<node TEXT="=ID_1162766946.text" ID="ID_574543985" CREATED="1610814777369" MODIFIED="1610815546363" LINK="#ID_1162766946">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1811713131" STARTINCLINATION="743;0;" ENDINCLINATION="743;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
<node TEXT="act" STYLE_REF="klein und grau" ID="ID_779416213" CREATED="1610873641131" MODIFIED="1610873641131"/>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_168607536" CREATED="1610873665757" MODIFIED="1610873665757">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_16508133" STARTINCLINATION="133;0;" ENDINCLINATION="133;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="..." STYLE_REF="klein und grau" ID="ID_412029778" CREATED="1541848916824" MODIFIED="1541848917746"/>
<node TEXT="map and node" STYLE_REF="klein und grau" ID="ID_137698064" CREATED="1541846699048" MODIFIED="1561010307574"/>
<node TEXT="." ID="ID_1600294885" CREATED="1505561368013" MODIFIED="1505561368676">
<node FOLDED="true" ID="ID_1854744536" CREATED="1505561368678" MODIFIED="1611154006603" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">node</font>&#160;<b>= Parent</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="&lt;&lt;" STYLE_REF="klein und grau" ID="ID_503725252" CREATED="1592223020954" MODIFIED="1592223023729">
<node TEXT="=ID_1125959904.text" ID="ID_1588262998" CREATED="1592223007141" MODIFIED="1592223007188" LINK="#ID_1125959904">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;&lt;" STYLE_REF="klein und grau" ID="ID_856233801" CREATED="1610814977768" MODIFIED="1610814978999">
<node TEXT="=ID_1376915101.text" ID="ID_831444030" CREATED="1610814971140" MODIFIED="1610814971160" LINK="#ID_1376915101">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1446306369" CREATED="1510577789654" MODIFIED="1510577795846">
<node TEXT="=ID_1799662911.text" ID="ID_997247129" CREATED="1510577800693" MODIFIED="1561910876743" LINK="#ID_1799662911">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1632982554" STARTINCLINATION="419;0;" ENDINCLINATION="419;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_303339895" CREATED="1505561368013" MODIFIED="1505561368676">
<node FOLDED="true" ID="ID_974566585" CREATED="1505561368678" MODIFIED="1611154006605" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">node</font>&#160;<b>= Next</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="scope" STYLE_REF="klein und grau" ID="ID_908226242" CREATED="1592375495662" MODIFIED="1592375498743">
<node TEXT="get next following sibling node" ID="ID_552590190" CREATED="1592375498759" MODIFIED="1592375522748"/>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1183244332" CREATED="1510577789654" MODIFIED="1510577795846">
<node TEXT="=ID_1799662911.text" ID="ID_1818342219" CREATED="1510577800693" MODIFIED="1561910876743" LINK="#ID_1799662911">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1632982554" STARTINCLINATION="419;0;" ENDINCLINATION="419;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_174357272" CREATED="1505561368013" MODIFIED="1505561368676">
<node FOLDED="true" ID="ID_909500943" CREATED="1505561368678" MODIFIED="1611154006605" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">node</font>&#160;<b>= getChildByIndex()</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="scope" STYLE_REF="klein und grau" ID="ID_1674806898" CREATED="1592375495662" MODIFIED="1592375498743">
<node TEXT="get child node by its sequence index" ID="ID_967741362" CREATED="1592375498759" MODIFIED="1592375653305"/>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1938567924" CREATED="1510577789654" MODIFIED="1510577795846">
<node TEXT="=ID_1799662911.text" ID="ID_949079962" CREATED="1510577800693" MODIFIED="1561910876743" LINK="#ID_1799662911">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1632982554" STARTINCLINATION="419;0;" ENDINCLINATION="419;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_422000299" CREATED="1505561368013" MODIFIED="1505561368676">
<node ID="ID_1351085557" CREATED="1505561368678" MODIFIED="1611154006606" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">list</font>&#160;<b>= Children</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="scope" STYLE_REF="klein und grau" ID="ID_1294785073" CREATED="1592375530319" MODIFIED="1592375532488">
<node TEXT="get all child nodes" ID="ID_167668134" CREATED="1592375532494" MODIFIED="1592375548751"/>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1678021896" CREATED="1510577789654" MODIFIED="1510577795846">
<node TEXT="list of" ID="ID_403547426" CREATED="1510593074483" MODIFIED="1510593077186">
<node TEXT="=ID_1799662911.text" ID="ID_1475992233" CREATED="1510577800693" MODIFIED="1561910876781" LINK="#ID_1799662911">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1632982554" STARTINCLINATION="491;0;" ENDINCLINATION="491;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_1092836201" CREATED="1505561368013" MODIFIED="1505561368676">
<node FOLDED="true" ID="ID_1498323229" CREATED="1505561368678" MODIFIED="1611154006606" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">bool</font>&#160;<b>= hasChildren</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1943361971" CREATED="1510577789654" MODIFIED="1510577795846">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_399325450" CREATED="1541843560724" MODIFIED="1541843562396">
<node TEXT="True" ID="ID_1032528284" CREATED="1541843552715" MODIFIED="1541843559786">
<font BOLD="true"/>
<node TEXT="in case there are children present" STYLE_REF="klein und grau" ID="ID_1576886038" CREATED="1541843563654" MODIFIED="1541843574496"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_1932814854" CREATED="1505561368013" MODIFIED="1505561368676">
<node FOLDED="true" ID="ID_1127185024" CREATED="1505561368678" MODIFIED="1611154006606" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">list</font>&#160;<b>= findChildren()</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="code" STYLE_REF="klein und grau" ID="ID_1164944800" CREATED="1561910665902" MODIFIED="1561910667123">
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_1992590347" CREATED="1510579710601" MODIFIED="1541843529006">
<node ID="ID_1497180738" CREATED="1510579713078" MODIFIED="1510651565272"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;id&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_297895904" CREATED="1561911489020" MODIFIED="1561911489039">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_726090177" STARTINCLINATION="346;0;" ENDINCLINATION="346;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_571259616" CREATED="1510651439185" MODIFIED="1541843530126">
<node ID="ID_1046604647" CREATED="1510651445412" MODIFIED="1510651565272"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;core&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_42136468" CREATED="1561911489040" MODIFIED="1561911489040">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_220574594" STARTINCLINATION="343;0;" ENDINCLINATION="343;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_1113417906" CREATED="1510651541460" MODIFIED="1541843530786">
<node ID="ID_792678057" CREATED="1510651471610" MODIFIED="1510651565288"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;attrib&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1391183732" CREATED="1561911489056" MODIFIED="1561911489056">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1492850233" STARTINCLINATION="342;0;" ENDINCLINATION="342;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_1574631230" CREATED="1510651543602" MODIFIED="1541843531206">
<node ID="ID_719378998" CREATED="1510651475698" MODIFIED="1510651565288"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;details&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_807216859" CREATED="1561911489071" MODIFIED="1561911489071">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_591996903" STARTINCLINATION="341;0;" ENDINCLINATION="341;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_6213195" CREATED="1510651546065" MODIFIED="1541843531556">
<node ID="ID_1716398723" CREATED="1510651480080" MODIFIED="1510651565288"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;notes&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_156837148" CREATED="1561911489071" MODIFIED="1561911489071">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1467019771" STARTINCLINATION="339;0;" ENDINCLINATION="339;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_109083619" CREATED="1510651548455" MODIFIED="1541843531886">
<node ID="ID_415158987" CREATED="1510651485793" MODIFIED="1510651565288"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;link&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_580106246" CREATED="1561911489087" MODIFIED="1561911489087">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_292217928" STARTINCLINATION="339;0;" ENDINCLINATION="339;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_1116864066" CREATED="1510651548455" MODIFIED="1541843531886">
<node ID="ID_384083011" CREATED="1510651485793" MODIFIED="1561885863697"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;icon&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_780787265" CREATED="1561911489087" MODIFIED="1561911489103">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_363866081" STARTINCLINATION="337;0;" ENDINCLINATION="337;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_1737365937" CREATED="1510651550294" MODIFIED="1541843532606">
<node ID="ID_872657973" CREATED="1510651487750" MODIFIED="1510651565288"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;bExact&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1352400674" CREATED="1561911489103" MODIFIED="1561911489103">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1956694388" STARTINCLINATION="336;0;" ENDINCLINATION="336;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1948006141" CREATED="1561911218133" MODIFIED="1561911219486">
<node TEXT="find list of nodes below node" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1794245028" CREATED="1561911219486" MODIFIED="1561911517925" MIN_WIDTH="200">
<node TEXT="&lt;&lt;" STYLE_REF="klein und grau" ID="ID_1382096384" CREATED="1561911260072" MODIFIED="1561911264072">
<node TEXT="=ID_1438826838.text" ID="ID_651697305" CREATED="1561911254147" MODIFIED="1561911254264" LINK="#ID_1438826838">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_1193057282" CREATED="1561911367516" MODIFIED="1561911368405">
<node TEXT="=ID_1497180738.text" ID="ID_726090177" CREATED="1561911453245" MODIFIED="1561911453368" LINK="#ID_1497180738">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_962970215" CREATED="1561911364717" MODIFIED="1561911365686">
<node TEXT="=ID_1046604647.text" ID="ID_220574594" CREATED="1561911453368" MODIFIED="1561911453468" LINK="#ID_1046604647">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_657622380" CREATED="1561911362510" MODIFIED="1561911363369">
<node TEXT="=ID_792678057.text" ID="ID_1492850233" CREATED="1561911453468" MODIFIED="1561911453568" LINK="#ID_792678057">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_495317143" CREATED="1561911354640" MODIFIED="1561911355608">
<node TEXT="=ID_719378998.text" ID="ID_591996903" CREATED="1561911453568" MODIFIED="1561911453653" LINK="#ID_719378998">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_1572680169" CREATED="1561911360270" MODIFIED="1561911361096">
<node TEXT="=ID_1716398723.text" ID="ID_1467019771" CREATED="1561911453653" MODIFIED="1561911453737" LINK="#ID_1716398723">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_1797182558" CREATED="1561911356909" MODIFIED="1561911358563">
<node TEXT="=ID_415158987.text" ID="ID_292217928" CREATED="1561911453737" MODIFIED="1561911453822" LINK="#ID_415158987">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_627038863" CREATED="1561911352243" MODIFIED="1561911353187">
<node TEXT="=ID_384083011.text" ID="ID_363866081" CREATED="1561911453822" MODIFIED="1561911453922" LINK="#ID_384083011">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_465567103" CREATED="1561911347533" MODIFIED="1561911349987">
<node TEXT="=ID_872657973.text" ID="ID_1956694388" CREATED="1561911453922" MODIFIED="1561911454001" LINK="#ID_872657973">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="call" STYLE_REF="klein und grau" ID="ID_1170261423" CREATED="1561911229221" MODIFIED="1561911239692">
<node TEXT="=ID_838144026.text" ID="ID_466316273" CREATED="1561911190261" MODIFIED="1561911677118" LINK="#ID_838144026">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_330698355" STARTINCLINATION="1655;0;" ENDINCLINATION="1655;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
<node TEXT="&gt;" STYLE_REF="klein und grau" ID="ID_1192765218" CREATED="1561911300786" MODIFIED="1561911303090">
<node ID="ID_265420130" CREATED="1561911303090" MODIFIED="1561911307030"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;lstNodes&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1950893830" CREATED="1561911654834" MODIFIED="1561911654834">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1997709556" STARTINCLINATION="90;0;" ENDINCLINATION="90;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_952710433" CREATED="1561910673047" MODIFIED="1561910675042">
<node TEXT="create Node instances" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1324128774" CREATED="1561910607073" MODIFIED="1561911289676" MIN_WIDTH="200">
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_465441527" CREATED="1561911659023" MODIFIED="1561911660405">
<node TEXT="=ID_265420130.text" ID="ID_1997709556" CREATED="1561911654743" MODIFIED="1561911654881" LINK="#ID_265420130">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="init" STYLE_REF="klein und grau" ID="ID_1381194097" CREATED="1561910677504" MODIFIED="1561910679847">
<node TEXT="=ID_645829533.text" ID="ID_1809526602" CREATED="1561910559145" MODIFIED="1561910572296" LINK="#ID_645829533">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1508706568" STARTINCLINATION="1160;0;" ENDINCLINATION="1160;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1994781258" CREATED="1510577789654" MODIFIED="1510577795846">
<node TEXT="list of" ID="ID_1006754830" CREATED="1510606395792" MODIFIED="1510606398376">
<node TEXT="=ID_1799662911.text" ID="ID_562145751" CREATED="1510577800693" MODIFIED="1561910876828" LINK="#ID_1799662911">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1632982554" STARTINCLINATION="706;0;" ENDINCLINATION="706;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_128632211" CREATED="1505561368013" MODIFIED="1505561368676">
<node ID="ID_362731513" CREATED="1505561368678" MODIFIED="1611154006607" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">list</font>&#160;<b>= findNodes()</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="code" STYLE_REF="klein und grau" ID="ID_577160247" CREATED="1561910683083" MODIFIED="1561910684250">
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_803534079" CREATED="1510579710601" MODIFIED="1541843529006">
<node ID="ID_1598484507" CREATED="1510579713078" MODIFIED="1510651565272"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;id&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1238602266" CREATED="1561911581867" MODIFIED="1561911581867">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1720300897" STARTINCLINATION="346;0;" ENDINCLINATION="346;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_678164257" CREATED="1510651439185" MODIFIED="1541843530126">
<node ID="ID_715713248" CREATED="1510651445412" MODIFIED="1510651565272"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;core&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1252800313" CREATED="1561911581883" MODIFIED="1561911581883">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1379583807" STARTINCLINATION="343;0;" ENDINCLINATION="343;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_1823345542" CREATED="1510651541460" MODIFIED="1541843530786">
<node ID="ID_445938122" CREATED="1510651471610" MODIFIED="1510651565288"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;attrib&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1187649342" CREATED="1561911581883" MODIFIED="1561911581898">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1758666451" STARTINCLINATION="342;0;" ENDINCLINATION="342;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_266429204" CREATED="1510651543602" MODIFIED="1541843531206">
<node ID="ID_712195684" CREATED="1510651475698" MODIFIED="1510651565288"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;details&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1016634825" CREATED="1561911581898" MODIFIED="1561911581898">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_645296979" STARTINCLINATION="341;0;" ENDINCLINATION="341;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_1918882407" CREATED="1510651546065" MODIFIED="1541843531556">
<node ID="ID_443926006" CREATED="1510651480080" MODIFIED="1510651565288"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;notes&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1281207181" CREATED="1561911581898" MODIFIED="1561911581898">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_730552100" STARTINCLINATION="339;0;" ENDINCLINATION="339;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_1701336783" CREATED="1510651548455" MODIFIED="1541843531886">
<node ID="ID_1225122477" CREATED="1510651485793" MODIFIED="1510651565288"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;link&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1339032979" CREATED="1561911581914" MODIFIED="1561911581914">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1036530778" STARTINCLINATION="339;0;" ENDINCLINATION="339;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_1585980593" CREATED="1510651548455" MODIFIED="1541843531886">
<node ID="ID_350002520" CREATED="1510651485793" MODIFIED="1561885863697"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;icon&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1814788596" CREATED="1561911581914" MODIFIED="1561911581914">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1034325914" STARTINCLINATION="337;0;" ENDINCLINATION="337;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_77308793" CREATED="1510651550294" MODIFIED="1541843532606">
<node ID="ID_1276767938" CREATED="1510651487750" MODIFIED="1510651565288"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;bExact&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1004080585" CREATED="1561911581914" MODIFIED="1561911581914">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_820998375" STARTINCLINATION="336;0;" ENDINCLINATION="336;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_189631162" CREATED="1561911218133" MODIFIED="1561911219486">
<node TEXT="find list of nodes directly below node" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1972302440" CREATED="1561911219486" MODIFIED="1561911641048" MIN_WIDTH="200">
<node TEXT="&lt;&lt;" STYLE_REF="klein und grau" ID="ID_1206946908" CREATED="1561911260072" MODIFIED="1561911264072">
<node TEXT="=ID_1438826838.text" ID="ID_1199442455" CREATED="1561911254147" MODIFIED="1561911254264" LINK="#ID_1438826838">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_426698425" CREATED="1561911367516" MODIFIED="1561911368405">
<node TEXT="=ID_1598484507.text" ID="ID_1720300897" CREATED="1561911556744" MODIFIED="1561911556896" LINK="#ID_1598484507">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_19841889" CREATED="1561911364717" MODIFIED="1561911365686">
<node TEXT="=ID_715713248.text" ID="ID_1379583807" CREATED="1561911556896" MODIFIED="1561911556980" LINK="#ID_715713248">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_834941365" CREATED="1561911362510" MODIFIED="1561911363369">
<node TEXT="=ID_445938122.text" ID="ID_1758666451" CREATED="1561911556980" MODIFIED="1561911557065" LINK="#ID_445938122">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_795631257" CREATED="1561911360270" MODIFIED="1561911361096">
<node TEXT="=ID_712195684.text" ID="ID_645296979" CREATED="1561911557065" MODIFIED="1561911557149" LINK="#ID_712195684">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_1904899568" CREATED="1561911356909" MODIFIED="1561911358563">
<node TEXT="=ID_443926006.text" ID="ID_730552100" CREATED="1561911557149" MODIFIED="1561911557244" LINK="#ID_443926006">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_988080000" CREATED="1561911354640" MODIFIED="1561911355608">
<node TEXT="=ID_1225122477.text" ID="ID_1036530778" CREATED="1561911557246" MODIFIED="1561911557327" LINK="#ID_1225122477">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_438296447" CREATED="1561911352243" MODIFIED="1561911353187">
<node TEXT="=ID_350002520.text" ID="ID_1034325914" CREATED="1561911557327" MODIFIED="1561911557411" LINK="#ID_350002520">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_3955232" CREATED="1561911347533" MODIFIED="1561911349987">
<node TEXT="=ID_1276767938.text" ID="ID_820998375" CREATED="1561911557411" MODIFIED="1561911557496" LINK="#ID_1276767938">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="call" STYLE_REF="klein und grau" ID="ID_619538625" CREATED="1561911229221" MODIFIED="1561911239692">
<node TEXT="=ID_838144026.text" ID="ID_662883710" CREATED="1561911190261" MODIFIED="1561911677165" LINK="#ID_838144026">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_330698355" STARTINCLINATION="1212;0;" ENDINCLINATION="1212;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
<node TEXT="&gt;" STYLE_REF="klein und grau" ID="ID_306152729" CREATED="1561911300786" MODIFIED="1561911303090">
<node ID="ID_224272939" CREATED="1561911303090" MODIFIED="1561911307030"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;lstNodes&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1955242927" CREATED="1561911663911" MODIFIED="1561911663911">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_376710546" STARTINCLINATION="90;0;" ENDINCLINATION="90;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_451228325" CREATED="1561910673047" MODIFIED="1561910675042">
<node TEXT="create Node instances" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_523355144" CREATED="1561910607073" MODIFIED="1561911289676" MIN_WIDTH="200">
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_612370414" CREATED="1561911668070" MODIFIED="1561911668944">
<node TEXT="=ID_224272939.text" ID="ID_376710546" CREATED="1561911663780" MODIFIED="1561911663958" LINK="#ID_224272939">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="init" STYLE_REF="klein und grau" ID="ID_14309994" CREATED="1561910677504" MODIFIED="1561910679847">
<node TEXT="=ID_645829533.text" ID="ID_1357331836" CREATED="1561910559145" MODIFIED="1561910572296" LINK="#ID_645829533">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1508706568" STARTINCLINATION="1160;0;" ENDINCLINATION="1160;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_328782437" CREATED="1510577789654" MODIFIED="1510577795846">
<node TEXT="list of" ID="ID_745806057" CREATED="1510606395792" MODIFIED="1510606398376">
<node TEXT="=ID_1799662911.text" ID="ID_422139910" CREATED="1510577800693" MODIFIED="1561910876881" LINK="#ID_1799662911">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1632982554" STARTINCLINATION="940;0;" ENDINCLINATION="940;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_1702883268" CREATED="1610788406800" MODIFIED="1610788408388">
<node ID="ID_744389609" CREATED="1610788408405" MODIFIED="1611154006607" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">node </font><b>= attach()</b>
  </body>
</html>
</richcontent>
<node TEXT="scope" STYLE_REF="klein und grau" ID="ID_1114447637" CREATED="1610789548910" MODIFIED="1610789550923">
<node TEXT="attach head node of detached branch below map or branch node" ID="ID_1447431321" CREATED="1610789550925" MODIFIED="1610902086063">
<node TEXT="enable &quot;move&quot; of map branches to other positions" STYLE_REF="ANFORDERUNG (extern)" ID="ID_695381407" CREATED="1610902097034" MODIFIED="1610902130507"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_1582743801" CREATED="1610789759324" MODIFIED="1610789764278">
<node ID="ID_1411681014" CREATED="1610789764799" MODIFIED="1610873934162"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;node&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1172087822" CREATED="1610874000010" MODIFIED="1610874000010">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1015016671" STARTINCLINATION="395;0;" ENDINCLINATION="395;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="code" STYLE_REF="klein und grau" ID="ID_512559249" CREATED="1610817306749" MODIFIED="1610817308069">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1304002165" CREATED="1610817534715" MODIFIED="1610817534717">
<node TEXT="check if attached node is valid" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1282580074" CREATED="1610817399712" MODIFIED="1610912215683" MIN_WIDTH="400"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1826312373" CREATED="1610817308729" MODIFIED="1610817310242">
<node TEXT="check if to-be-attached-node is already attached" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1274827447" CREATED="1610817310248" MODIFIED="1610912215683" MIN_WIDTH="400">
<node TEXT="&lt;&lt;" STYLE_REF="klein und grau" ID="ID_1302108036" CREATED="1610817385357" MODIFIED="1610817387063">
<node TEXT="=ID_1125959904.text" ID="ID_983098355" CREATED="1610817366347" MODIFIED="1610817366357" LINK="#ID_1125959904">
<attribute NAME="use_node_for" VALUE="reference"/>
<node TEXT="from MAP" STYLE_REF="klein und grau" ID="ID_990525608" CREATED="1610817612789" MODIFIED="1610817615630"/>
</node>
</node>
<node TEXT="&lt;&lt;" STYLE_REF="klein und grau" ID="ID_1618613991" CREATED="1610817388426" MODIFIED="1610817389659">
<node TEXT="=ID_1376915101.text" ID="ID_1062094229" CREATED="1610817366328" MODIFIED="1610817366347" LINK="#ID_1376915101">
<attribute NAME="use_node_for" VALUE="reference"/>
<node TEXT="from BRANCH" STYLE_REF="klein und grau" ID="ID_1141338510" CREATED="1610817602868" MODIFIED="1610817607550"/>
</node>
</node>
</node>
</node>
<node TEXT="DIFFERENT CASES" STYLE_REF="klein und grau" ID="ID_1202293834" CREATED="1610906650100" MODIFIED="1610906655242"/>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1767137308" CREATED="1610817534721" MODIFIED="1610817534722">
<node TEXT="handle attach of detached head to map node" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1051044431" CREATED="1610817446026" MODIFIED="1610912215683" MIN_WIDTH="400"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_212192626" CREATED="1610910970457" MODIFIED="1610910971300">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1536760716" CREATED="1610817534727" MODIFIED="1610817534728">
<node TEXT="update old branch head&apos;s _map member" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_624205190" CREATED="1610817456789" MODIFIED="1610912215683" MIN_WIDTH="400">
<node TEXT="&lt;&lt;" STYLE_REF="klein und grau" ID="ID_1372630091" CREATED="1610873594217" MODIFIED="1610873595632">
<node TEXT="=ID_1554808123.text" ID="ID_1379150542" CREATED="1610873586555" MODIFIED="1610873586581" LINK="#ID_1554808123">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&gt;&gt;" STYLE_REF="klein und grau" ID="ID_288948975" CREATED="1610817568143" MODIFIED="1610817569682">
<node TEXT="=ID_1257855042.text" ID="ID_4208596" CREATED="1610873618155" MODIFIED="1610873618171" LINK="#ID_1257855042">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1554020873" STARTINCLINATION="109;0;" ENDINCLINATION="109;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
<node TEXT="&gt;&gt;" STYLE_REF="klein und grau" ID="ID_1150204693" CREATED="1610873647428" MODIFIED="1610873648544">
<node TEXT="=ID_1984205011.text" ID="ID_16508133" CREATED="1610873665757" MODIFIED="1610873665772" LINK="#ID_1984205011">
<attribute NAME="use_node_for" VALUE="reference"/>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_211188143" CREATED="1610873688281" MODIFIED="1610873689663">
<node TEXT="=ID_319634852.text" ID="ID_516848659" CREATED="1610873677485" MODIFIED="1610874025370" LINK="#ID_319634852">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_740997091" STARTINCLINATION="1292;0;" ENDINCLINATION="1292;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
<node TEXT="UPDATE in BRANCH" STYLE_REF="klein und grau" ID="ID_458994973" CREATED="1610873187874" MODIFIED="1610874080315"/>
</node>
</node>
</node>
</node>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1082060932" CREATED="1610910973159" MODIFIED="1610910974156">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_623941464" CREATED="1610817534733" MODIFIED="1610817534735">
<node TEXT="set parent node within map&apos;s parentmap" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1427915874" CREATED="1610817475235" MODIFIED="1610912215683" MIN_WIDTH="400">
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_796401043" CREATED="1610817388426" MODIFIED="1610873909748">
<node TEXT="=ID_645829533.text" ID="ID_1024840865" CREATED="1610873855953" MODIFIED="1610873855972" LINK="#ID_645829533">
<attribute NAME="use_node_for" VALUE="reference"/>
<node TEXT="as new parent node" STYLE_REF="klein und grau" ID="ID_703417480" CREATED="1610873962141" MODIFIED="1610873977185"/>
</node>
</node>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_24883982" CREATED="1610873910958" MODIFIED="1610873914749">
<node TEXT="=ID_1411681014.text" ID="ID_1015016671" CREATED="1610873936076" MODIFIED="1610873936092" LINK="#ID_1411681014">
<attribute NAME="use_node_for" VALUE="reference"/>
<node TEXT="as node to be attached" STYLE_REF="klein und grau" ID="ID_367163276" CREATED="1610873985958" MODIFIED="1610873991760"/>
</node>
</node>
<node TEXT="&gt;&gt;" STYLE_REF="klein und grau" ID="ID_1549489247" CREATED="1610817563077" MODIFIED="1610817566489">
<node TEXT="=ID_319634852.text" ID="ID_605939720" CREATED="1610873722269" MODIFIED="1610873722269" LINK="#ID_319634852">
<attribute NAME="use_node_for" VALUE="reference"/>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_653528690" CREATED="1610873757615" MODIFIED="1610873759176">
<node TEXT="=ID_1125959904.text" ID="ID_234310101" CREATED="1610817546391" MODIFIED="1610817546407" LINK="#ID_1125959904">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_265888356" STARTINCLINATION="169;0;" ENDINCLINATION="169;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
<node TEXT="UPDATE in MAP" STYLE_REF="klein und grau" ID="ID_1099883171" CREATED="1610817612789" MODIFIED="1610874087877"/>
</node>
</node>
</node>
</node>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1587407611" CREATED="1610910975993" MODIFIED="1610910977494">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1120206405" CREATED="1610873410991" MODIFIED="1610873413215">
<node TEXT="append map&apos;s parent dict from branch&apos;s dict" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_688947813" CREATED="1610873413215" MODIFIED="1610912215683" MIN_WIDTH="400"/>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1735973958" CREATED="1610910975993" MODIFIED="1610910977494">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1236482040" CREATED="1610873410991" MODIFIED="1610873413215">
<node TEXT="save new map reference in old branch object" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1431164947" CREATED="1610873413215" MODIFIED="1610912215683" MIN_WIDTH="400"/>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1961200957" CREATED="1610912319342" MODIFIED="1610912320794">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1991159422" CREATED="1610910889035" MODIFIED="1610910890835">
<node TEXT="insert appropriate XML nodes" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1415184133" CREATED="1610910890835" MODIFIED="1610912215683" MIN_WIDTH="400"/>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1306451693" CREATED="1610817534721" MODIFIED="1610817534722">
<node TEXT="handle attach of detached head to detached branch" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1461383488" CREATED="1610817446026" MODIFIED="1610912215683" MIN_WIDTH="400"/>
</node>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1783766113" CREATED="1510577789654" MODIFIED="1510577795846">
<node TEXT="=ID_1799662911.text" ID="ID_1012762288" CREATED="1510577800693" MODIFIED="1561910876981" LINK="#ID_1799662911">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1632982554" STARTINCLINATION="1740;0;" ENDINCLINATION="1740;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_1400266296" CREATED="1610788406800" MODIFIED="1610788408388">
<node STYLE_REF="ANFORDERUNG (extern)" ID="ID_622286792" CREATED="1610788408405" MODIFIED="1610897117934" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">node </font><b>= detach()</b>
  </body>
</html>
</richcontent>
<node TEXT="scope" STYLE_REF="klein und grau" ID="ID_1363855231" CREATED="1610789548910" MODIFIED="1610789550923">
<node TEXT="detach node / tree from mindmap" ID="ID_1983896039" CREATED="1610789550925" MODIFIED="1610897137565"/>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1256719857" CREATED="1510577789654" MODIFIED="1510577795846">
<node TEXT="=ID_1799662911.text" ID="ID_1305155323" CREATED="1510577800693" MODIFIED="1561910876981" LINK="#ID_1799662911">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1632982554" STARTINCLINATION="1740;0;" ENDINCLINATION="1740;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_1715760490" CREATED="1561010310732" MODIFIED="1561010311957">
<node FOLDED="true" ID="ID_1726108232" CREATED="1561010357597" MODIFIED="1611154006607" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">node</font><b>&#160;= addChild( </b><font color="#0000ff">[ &lt;option&gt; [ </font><b>, </b><font color="#0000ff">] ]+</font><b>&#160;)</b>
  </body>
</html>
</richcontent>
<node TEXT="&lt;option&gt;" STYLE_REF="klein und grau" ID="ID_1545131733" CREATED="1561010404877" MODIFIED="1561010416958">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_249703038" CREATED="1561010530799" MODIFIED="1561010530799">
<node ID="ID_19119610" CREATED="1561010527820" MODIFIED="1561893818453" MIN_WIDTH="160"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <b>core=</b><font color="#0000ff">&lt;string&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="&lt;string&gt;" STYLE_REF="klein und grau" ID="ID_1286781105" CREATED="1561010527820" MODIFIED="1561010541832" MIN_WIDTH="80">
<node TEXT="new node&apos;s core text string" ID="ID_1215575744" CREATED="1561010619787" MODIFIED="1561010633037"/>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1586039473" CREATED="1561010530815" MODIFIED="1561010530815">
<node ID="ID_1762520812" CREATED="1561010527805" MODIFIED="1561010535599" MIN_WIDTH="160"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <b>style=</b><font color="#0000ff">&lt;string&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="&lt;string&gt;" STYLE_REF="klein und grau" ID="ID_1457578928" CREATED="1561010527805" MODIFIED="1561010541832" MIN_WIDTH="80">
<node TEXT="=ID_180520672.text" ID="ID_1667751251" CREATED="1610692124300" MODIFIED="1610692124334" LINK="#ID_180520672">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1759812947" CREATED="1561010595244" MODIFIED="1561010597804">
<node TEXT="klein und grau" ID="ID_821207340" CREATED="1561010597804" MODIFIED="1561010601859">
<font BOLD="true"/>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1736154132" CREATED="1561010603614" MODIFIED="1561010604691">
<node TEXT="comment" ID="ID_415106840" CREATED="1561010604691" MODIFIED="1561010607450">
<font BOLD="true"/>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_486783517" CREATED="1561010608130" MODIFIED="1561010609220">
<node TEXT="..." ID="ID_1075721240" CREATED="1561010609220" MODIFIED="1561010613358"/>
</node>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_391436031" CREATED="1561010530815" MODIFIED="1561010530815">
<node ID="ID_1446734381" CREATED="1561010527773" MODIFIED="1561010535599" MIN_WIDTH="160"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <b>pos=</b><font color="#0000ff">&lt;idx&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="&lt;idx&gt;" STYLE_REF="klein und grau" ID="ID_1088907215" CREATED="1561010527789" MODIFIED="1561010541832" MIN_WIDTH="80">
<node TEXT="position among other siblings" ID="ID_360649701" CREATED="1561010560766" MODIFIED="1610692198997">
<node TEXT="starting at 0" STYLE_REF="klein und grau" ID="ID_564617031" CREATED="1561010583938" MODIFIED="1561010587830"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_202307558" CREATED="1561010784943" MODIFIED="1561010790217">
<node TEXT="-1" OBJECT="java.lang.Long|-1" ID="ID_1813967939" CREATED="1561010791033" MODIFIED="1561010794124">
<font BOLD="true"/>
<node TEXT="last position, [ DEFAULT ]" STYLE_REF="klein und grau" ID="ID_1046709113" CREATED="1561010795387" MODIFIED="1610692156818"/>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1548313242" CREATED="1561010824616" MODIFIED="1561010825875">
<node TEXT="0" OBJECT="java.lang.Long|0" ID="ID_830049304" CREATED="1561010825875" MODIFIED="1561010829047">
<font BOLD="true"/>
<node TEXT="first position" STYLE_REF="klein und grau" ID="ID_717936063" CREATED="1561010829426" MODIFIED="1561010832950"/>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1530068200" CREATED="1561010835248" MODIFIED="1561010837065">
<node TEXT="1" OBJECT="java.lang.Long|1" ID="ID_196887789" CREATED="1561010837065" MODIFIED="1561010841799">
<font BOLD="true"/>
<node TEXT="2nd position" STYLE_REF="klein und grau" ID="ID_1101710915" CREATED="1561010842737" MODIFIED="1561010846304"/>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1853063434" CREATED="1561010852616" MODIFIED="1561010853643">
<node TEXT="..." ID="ID_1099614271" CREATED="1561010853643" MODIFIED="1561010855346"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="code" STYLE_REF="klein und grau" ID="ID_1494335738" CREATED="1561909483254" MODIFIED="1561909485157">
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_1815862140" CREATED="1561909614297" MODIFIED="1561909617105">
<node ID="ID_759183744" CREATED="1561909617108" MODIFIED="1561910855473"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;core&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1557091708" CREATED="1561910857361" MODIFIED="1561910857361">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_959332792" STARTINCLINATION="306;0;" ENDINCLINATION="306;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_1840604946" CREATED="1610817765689" MODIFIED="1610817766849">
<node ID="ID_1476617369" CREATED="1610817767504" MODIFIED="1610817770504"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;link&gt;</font>
  </body>
</html>
</richcontent>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_279630124" CREATED="1610817945232" MODIFIED="1610817946174">
<node ID="ID_1060296274" CREATED="1610817946983" MODIFIED="1610817948554"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;id&gt;</font>
  </body>
</html>
</richcontent>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_1676732155" CREATED="1561909655763" MODIFIED="1561909658766">
<node ID="ID_540711007" CREATED="1561909658766" MODIFIED="1561910855473"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;pos&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_990011271" CREATED="1561910857377" MODIFIED="1561910857377">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_448788471" STARTINCLINATION="326;0;" ENDINCLINATION="326;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_1527139412" CREATED="1561909662460" MODIFIED="1561909664062">
<node ID="ID_1983406933" CREATED="1561909664062" MODIFIED="1561910855473"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;style&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1279321331" CREATED="1561910857392" MODIFIED="1561910857392">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_834157448" STARTINCLINATION="325;0;" ENDINCLINATION="325;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1621731195" CREATED="1561909485157" MODIFIED="1561909487566">
<node TEXT="create and init element" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_406845121" CREATED="1561909487566" MODIFIED="1561909690123" MIN_WIDTH="260">
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_1740846495" CREATED="1561909624530" MODIFIED="1561909625467">
<node TEXT="=ID_759183744.text" ID="ID_959332792" CREATED="1561909619986" MODIFIED="1561909620128" LINK="#ID_759183744">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;&lt;" STYLE_REF="klein und grau" ID="ID_1603956283" CREATED="1561909599739" MODIFIED="1561909601973">
<node TEXT="=ID_1257855042.text" ID="ID_306460805" CREATED="1561909586572" MODIFIED="1561909586724" LINK="#ID_1257855042">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="init" STYLE_REF="klein und grau" ID="ID_1257427161" CREATED="1561910428746" MODIFIED="1561910432047">
<node TEXT="=ID_645829533.text" ID="ID_1017279416" CREATED="1561910559145" MODIFIED="1610692158435" LINK="#ID_645829533">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1508706568" STARTINCLINATION="1160;0;" ENDINCLINATION="1160;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_609855600" CREATED="1610817736266" MODIFIED="1610817736267">
<node TEXT="overwrite standard id" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1366904272" CREATED="1610817727380" MODIFIED="1610817734981"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1341153384" CREATED="1610817757311" MODIFIED="1610817757312">
<node TEXT="set link portion" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_417784698" CREATED="1610817751402" MODIFIED="1610817756950"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1796397061" CREATED="1561909531099" MODIFIED="1561909532237">
<node TEXT="set node&apos;s position within children" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_10762627" CREATED="1561909507740" MODIFIED="1561909690123" MIN_WIDTH="260">
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_1690267510" CREATED="1561909684137" MODIFIED="1561909685122">
<node TEXT="=ID_540711007.text" ID="ID_448788471" CREATED="1561909670684" MODIFIED="1561909670851" LINK="#ID_540711007">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_441282114" CREATED="1561909535375" MODIFIED="1561909536240">
<node TEXT="set style" ID="ID_498762571" CREATED="1561909514079" MODIFIED="1561909690123" MIN_WIDTH="260">
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_222660448" CREATED="1561909680785" MODIFIED="1561909681888">
<node TEXT="=ID_1983406933.text" ID="ID_834157448" CREATED="1561909670851" MODIFIED="1561909670952" LINK="#ID_1983406933">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_115697417" CREATED="1561909537837" MODIFIED="1561909538664">
<node TEXT="update parentmap dict" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_621744797" CREATED="1561909519211" MODIFIED="1610819066978" MIN_WIDTH="260">
<node TEXT="&gt;&gt;" STYLE_REF="klein und grau" ID="ID_1508045698" CREATED="1592223121145" MODIFIED="1592223126439">
<node TEXT="=ID_1125959904.text" ID="ID_1145714350" CREATED="1592223073132" MODIFIED="1592223176815" LINK="#ID_1125959904">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_265888356" STARTINCLINATION="1989;0;" ENDINCLINATION="1989;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
<node TEXT="for MAP" STYLE_REF="klein und grau" ID="ID_411680995" CREATED="1610817612789" MODIFIED="1610817623463"/>
</node>
</node>
<node TEXT="&gt;&gt;" STYLE_REF="klein und grau" ID="ID_1019433168" CREATED="1610817884633" MODIFIED="1610817892205">
<node TEXT="=ID_1376915101.text" ID="ID_1372781269" CREATED="1610814969011" MODIFIED="1610818439905" LINK="#ID_1376915101">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_294932515" STARTINCLINATION="1887;0;" ENDINCLINATION="1887;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
<node TEXT="for BRANCH" STYLE_REF="klein und grau" ID="ID_1766194900" CREATED="1610817888011" MODIFIED="1610817891516"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1668492217" CREATED="1510577789654" MODIFIED="1510577795846">
<node TEXT="=ID_1799662911.text" ID="ID_1755593377" CREATED="1510577800693" MODIFIED="1561910876944" LINK="#ID_1799662911">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1632982554" STARTINCLINATION="1444;0;" ENDINCLINATION="1444;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_333376205" CREATED="1561010310732" MODIFIED="1561010311957">
<node FOLDED="true" ID="ID_390338995" CREATED="1561010357597" MODIFIED="1611154006616" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">node</font><b>&#160;= addSibling( </b><font color="#0000ff">[ &lt;option&gt; [ </font><b>, </b><font color="#0000ff">] ]+</font><b>&#160;)</b>
  </body>
</html>
</richcontent>
<node TEXT="&lt;option&gt;" STYLE_REF="klein und grau" ID="ID_194113454" CREATED="1561010404877" MODIFIED="1561013779572" LINK="#ID_1545131733"/>
<node TEXT="code" STYLE_REF="klein und grau" ID="ID_1105496412" CREATED="1561910403676" MODIFIED="1561910405085">
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_1302860326" CREATED="1561909614297" MODIFIED="1561909617105">
<node ID="ID_281347254" CREATED="1561909617108" MODIFIED="1561909619359"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;core&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_314901783" CREATED="1561910842624" MODIFIED="1561910842624">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1838076745" STARTINCLINATION="306;0;" ENDINCLINATION="306;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_699914211" CREATED="1610817765689" MODIFIED="1610817766849">
<node ID="ID_302247002" CREATED="1610817767504" MODIFIED="1610817770504"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;link&gt;</font>
  </body>
</html>
</richcontent>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_427656766" CREATED="1610817945232" MODIFIED="1610817946174">
<node ID="ID_1757189948" CREATED="1610817946983" MODIFIED="1610817948554"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;id&gt;</font>
  </body>
</html>
</richcontent>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_943738105" CREATED="1561909655763" MODIFIED="1561909658766">
<node ID="ID_1778258256" CREATED="1561909658766" MODIFIED="1561909661231"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;pos&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1687926179" CREATED="1561910842655" MODIFIED="1561910842656">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_63480097" STARTINCLINATION="326;0;" ENDINCLINATION="326;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_368746940" CREATED="1561909662460" MODIFIED="1561909664062">
<node ID="ID_878907509" CREATED="1561909664062" MODIFIED="1561909667444"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;style&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="ref" STYLE_REF="klein und grau" ID="ID_1588004063" CREATED="1561910842656" MODIFIED="1561910842656">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_26172195" STARTINCLINATION="325;0;" ENDINCLINATION="325;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1767831434" CREATED="1561909485157" MODIFIED="1561909487566">
<node TEXT="create and init element" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_772446751" CREATED="1561909487566" MODIFIED="1561909690123" MIN_WIDTH="260">
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_673590837" CREATED="1561909624530" MODIFIED="1561909625467">
<node TEXT="=ID_281347254.text" ID="ID_1838076745" CREATED="1561910789701" MODIFIED="1561910789856" LINK="#ID_281347254">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="&lt;&lt;" STYLE_REF="klein und grau" ID="ID_1065521655" CREATED="1561909599739" MODIFIED="1561909601973">
<node TEXT="=ID_1257855042.text" ID="ID_953738819" CREATED="1561909586572" MODIFIED="1561909586724" LINK="#ID_1257855042">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
<node TEXT="init" STYLE_REF="klein und grau" ID="ID_478945621" CREATED="1561910428746" MODIFIED="1561910432047">
<node TEXT="=ID_645829533.text" ID="ID_1118966107" CREATED="1561910559145" MODIFIED="1561910572296" LINK="#ID_645829533">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1508706568" STARTINCLINATION="1160;0;" ENDINCLINATION="1160;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1214010875" CREATED="1610817736266" MODIFIED="1610817736267">
<node TEXT="overwrite standard id" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_541232914" CREATED="1610817727380" MODIFIED="1610817734981"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_604583569" CREATED="1610817757311" MODIFIED="1610817757312">
<node TEXT="set link portion" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_170172895" CREATED="1610817751402" MODIFIED="1610817756950"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_95572926" CREATED="1561909531099" MODIFIED="1561909532237">
<node TEXT="set node&apos;s position within siblings" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1899364114" CREATED="1561909507740" MODIFIED="1561910833510" MIN_WIDTH="260">
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_978106936" CREATED="1561909684137" MODIFIED="1561909685122">
<node TEXT="=ID_1778258256.text" ID="ID_63480097" CREATED="1561910789856" MODIFIED="1561910789941" LINK="#ID_1778258256">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1410065466" CREATED="1561909535375" MODIFIED="1561909536240">
<node TEXT="set style" ID="ID_1140168444" CREATED="1561909514079" MODIFIED="1561909690123" MIN_WIDTH="260">
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_1511511818" CREATED="1561909680785" MODIFIED="1561909681888">
<node TEXT="=ID_878907509.text" ID="ID_26172195" CREATED="1561910789941" MODIFIED="1561910790025" LINK="#ID_878907509">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1399339494" CREATED="1561909537837" MODIFIED="1561909538664">
<node TEXT="update parentmap dict" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_191831258" CREATED="1561909519211" MODIFIED="1610819073136" MIN_WIDTH="260">
<node TEXT="&gt;&gt;" STYLE_REF="klein und grau" ID="ID_430120706" CREATED="1592223121145" MODIFIED="1592223126439">
<node TEXT="=ID_1125959904.text" ID="ID_564192134" CREATED="1592223073132" MODIFIED="1592223176830" LINK="#ID_1125959904">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_265888356" STARTINCLINATION="2280;0;" ENDINCLINATION="2280;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
<node TEXT="for MAP" STYLE_REF="klein und grau" ID="ID_1569004672" CREATED="1610817612789" MODIFIED="1610817623463"/>
</node>
</node>
<node TEXT="&gt;&gt;" STYLE_REF="klein und grau" ID="ID_959229753" CREATED="1610817884633" MODIFIED="1610817892205">
<node TEXT="=ID_1376915101.text" ID="ID_163711530" CREATED="1610814969011" MODIFIED="1610818439914" LINK="#ID_1376915101">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_294932515" STARTINCLINATION="2309;0;" ENDINCLINATION="2309;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
<node TEXT="for BRANCH" STYLE_REF="klein und grau" ID="ID_594002428" CREATED="1610817888011" MODIFIED="1610817891516"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_832272395" CREATED="1510577789654" MODIFIED="1510577795846">
<node TEXT="=ID_1799662911.text" ID="ID_1395908089" CREATED="1510577800693" MODIFIED="1561910876981" LINK="#ID_1799662911">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1632982554" STARTINCLINATION="1740;0;" ENDINCLINATION="1740;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_1296534254" CREATED="1611153953491" MODIFIED="1611166442103">
<node ID="ID_720382307" CREATED="1611153954436" MODIFIED="1611173917074" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">bool </font><b>= addArrowLink( </b><font color="#0000ff">[</font><b> </b><font color="#0000ff">&lt;option&gt;</font><b> </b><font color="#0000ff">[</font><b> , </b><font color="#0000ff">]</font><b> </b><font color="#0000ff">]+</font><b> )</b>
  </body>
</html>

</richcontent>
<node TEXT="&lt;option&gt;" STYLE_REF="klein und grau" ID="ID_511722372" CREATED="1611154001570" MODIFIED="1611154001571">
<node ID="ID_906624054" CREATED="1611154028286" MODIFIED="1611160013527"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <b>node=</b><font color="#0000ff">&lt;node&gt;</font>
  </body>
</html>

</richcontent>
<node TEXT="&lt;node&gt;" STYLE_REF="klein und grau" ID="ID_960684652" CREATED="1611160013529" MODIFIED="1611160013530">
<node TEXT="=ID_645829533.text" ID="ID_1612959926" CREATED="1610873855953" MODIFIED="1610873855972" LINK="#ID_645829533">
<attribute NAME="use_node_for" VALUE="reference"/>
<node TEXT="as link&apos;s target" STYLE_REF="klein und grau" ID="ID_629363601" CREATED="1611160100059" MODIFIED="1611160109220"/>
</node>
</node>
</node>
<node STYLE_REF="ANFORDERUNG (extern)" ID="ID_1449217527" CREATED="1611154063300" MODIFIED="1611173923067"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <b>style=</b><font color="#0000ff">&lt;style&gt;</font>
  </body>
</html>

</richcontent>
<node TEXT="&lt;style&gt;" STYLE_REF="klein und grau" ID="ID_393932822" CREATED="1611160013538" MODIFIED="1611160013540">
<node TEXT="arrow style name" ID="ID_1031162397" CREATED="1611160019143" MODIFIED="1611160032893"/>
</node>
</node>
<node TEXT="" ID="ID_1336202975" CREATED="1611166089219" MODIFIED="1611166089219"/>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_527432606" CREATED="1611154001572" MODIFIED="1611154001573">
<node TEXT="True" ID="ID_1961175345" CREATED="1611160073482" MODIFIED="1611160080120">
<font BOLD="true"/>
<node TEXT="if arrow link could be established" STYLE_REF="klein und grau" ID="ID_1167126062" CREATED="1611160080851" MODIFIED="1611160089847"/>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_1272535374" CREATED="1611153953491" MODIFIED="1611166442103">
<node STYLE_REF="ANFORDERUNG (extern)" ID="ID_1632973088" CREATED="1611153954436" MODIFIED="1611173911674" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">list </font><b>= ArrowLinkTargets</b>
  </body>
</html>

</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1517578178" CREATED="1611154001572" MODIFIED="1611154001573">
<node TEXT="list of" ID="ID_1814685463" CREATED="1510593074483" MODIFIED="1510593077186">
<node TEXT="=ID_1799662911.text" ID="ID_1213777300" CREATED="1510577800693" MODIFIED="1561910876781" LINK="#ID_1799662911">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1632982554" STARTINCLINATION="491;0;" ENDINCLINATION="491;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="..." STYLE_REF="klein und grau" ID="ID_32488815" CREATED="1541846703238" MODIFIED="1541846708500"/>
<node TEXT="core" STYLE_REF="klein und grau" ID="ID_1319625885" CREATED="1505561982974" MODIFIED="1510557093260"/>
<node TEXT="." ID="ID_784050695" CREATED="1505560857665" MODIFIED="1505560858680">
<node ID="ID_912228982" CREATED="1505557603170" MODIFIED="1611154006619" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">string</font>&#160;<b>= Id</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1433948126" CREATED="1505557986359" MODIFIED="1589961590484">
<node TEXT="plain text ID string of node" ID="ID_845155991" CREATED="1505559793570" MODIFIED="1589961601433"/>
</node>
</node>
</node>
<node TEXT="." ID="ID_1417101743" CREATED="1505560857665" MODIFIED="1505560858680">
<node FOLDED="true" ID="ID_830382634" CREATED="1505557603170" MODIFIED="1611154006619" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">string</font>&#160;<b>= PlainText</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="code" STYLE_REF="klein und grau" ID="ID_1681883077" CREATED="1505558089546" MODIFIED="1505558092114">
<node TEXT="call" STYLE_REF="klein und grau" ID="ID_1305119090" CREATED="1510562926542" MODIFIED="1510562929197">
<node TEXT="=ID_408460964.text" ID="ID_993989632" CREATED="1510562938606" MODIFIED="1510563005131" LINK="#ID_408460964">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1619020964" STARTINCLINATION="605;0;" ENDINCLINATION="605;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
<node TEXT="sets / returns" STYLE_REF="klein und grau" ID="ID_736269696" CREATED="1505557986359" MODIFIED="1561840552543">
<node TEXT="plain text block from node&apos;s core or core HTML portion" ID="ID_1055945649" CREATED="1505559793570" MODIFIED="1505559822666"/>
</node>
</node>
</node>
<node TEXT="." ID="ID_542177126" CREATED="1505560857665" MODIFIED="1505560858680">
<node STYLE_REF="ANFORDERUNG (extern)" ID="ID_246211219" CREATED="1505557603170" MODIFIED="1610868450879" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">string</font>&#160;<b>= HtmlText</b>
    </p>
  </body>
</html>
</richcontent>
</node>
</node>
<node TEXT="." ID="ID_1806685201" CREATED="1505560857665" MODIFIED="1505560858680">
<node STYLE_REF="ANFORDERUNG (extern)" FOLDED="true" ID="ID_1086451219" CREATED="1505557603170" MODIFIED="1610868450879" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">string</font>&#160;<b>= Comment</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_652619284" CREATED="1505557986359" MODIFIED="1505557989115">
<node TEXT="comment string of node instance" ID="ID_1338605479" CREATED="1505559793570" MODIFIED="1510559268368"/>
</node>
</node>
</node>
<node TEXT="." ID="ID_1020758118" CREATED="1505561368013" MODIFIED="1505561368676">
<node FOLDED="true" ID="ID_187403699" CREATED="1505561368678" MODIFIED="1611154006620" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">bool</font>&#160;<b>= isComment</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_750361742" CREATED="1510577789654" MODIFIED="1510577795846">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_233709416" CREATED="1541843560724" MODIFIED="1541843562396">
<node TEXT="True" ID="ID_1111574255" CREATED="1541843552715" MODIFIED="1541843559786">
<font BOLD="true"/>
<node TEXT="in case the node is classified as &quot;comment&quot; node" STYLE_REF="klein und grau" ID="ID_140905205" CREATED="1541843563654" MODIFIED="1541843601697"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_1737681360" CREATED="1505560857665" MODIFIED="1505560858680">
<node FOLDED="true" ID="ID_1233177609" CREATED="1505557603170" MODIFIED="1611154006620" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">string</font>&#160;<b>= getSubText()</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="o" STYLE_REF="klein und grau" ID="ID_981295145" CREATED="1510577562853" MODIFIED="1510577577872">
<node ID="ID_751662174" CREATED="1510563272591" MODIFIED="1510577558087"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">&lt;token&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="token string to define necessary intermediate node core" ID="ID_40606805" CREATED="1510563277631" MODIFIED="1510563301077"/>
</node>
</node>
<node TEXT="code" STYLE_REF="klein und grau" ID="ID_1574731715" CREATED="1505558089546" MODIFIED="1505558092114">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1656601807" CREATED="1510563335759" MODIFIED="1510563336510">
<node TEXT="find node&apos;s INTERMEDIATE child node" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_629911282" CREATED="1510563337536" MODIFIED="1510577523539" MIN_WIDTH="300"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_245657629" CREATED="1510563370608" MODIFIED="1510563371439">
<node TEXT="access text portion of target node" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1909495674" CREATED="1510563372240" MODIFIED="1510577523539" MIN_WIDTH="300">
<node TEXT="call" STYLE_REF="klein und grau" ID="ID_279866241" CREATED="1510562926542" MODIFIED="1510562929197">
<node TEXT="=ID_408460964.text" ID="ID_601928291" CREATED="1510562938606" MODIFIED="1510563005131" LINK="#ID_408460964">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1619020964" STARTINCLINATION="605;0;" ENDINCLINATION="605;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1739241247" CREATED="1505557986359" MODIFIED="1505557989115">
<node TEXT="text portion of child&apos;s child node" ID="ID_1822082750" CREATED="1505559793570" MODIFIED="1510563037496"/>
</node>
</node>
</node>
<node TEXT="..." STYLE_REF="klein und grau" ID="ID_995718104" CREATED="1510940241241" MODIFIED="1510940242466"/>
<node TEXT="date and time" STYLE_REF="klein und grau" ID="ID_433713471" CREATED="1563010531889" MODIFIED="1563010536744"/>
<node TEXT="." ID="ID_1928184133" CREATED="1563010540590" MODIFIED="1563010541632">
<node FOLDED="true" ID="ID_436364483" CREATED="1563010610275" MODIFIED="1611154006620" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">tuple </font><b>= CreationDate</b>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_166040683" CREATED="1563010610306" MODIFIED="1563016017893">
<node TEXT="date and time (in local time system) when node was created" ID="ID_309011812" CREATED="1563016020705" MODIFIED="1563016057099"/>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1047451671" CREATED="1563016079839" MODIFIED="1563016081519">
<node ID="ID_716803623" CREATED="1563016119867" MODIFIED="1563016119883"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <b>( </b><font color="#0000ff">&lt;year&gt;</font><b>, </b><font color="#0000ff">&lt;month&gt;</font><b>, </b><font color="#0000ff">&lt;day&gt;</font><b>, </b><font color="#0000ff">&lt;hour&gt;</font><b>, </b><font color="#0000ff">&lt;minute&gt;</font><b>, </b><font color="#0000ff">&lt;second&gt;</font><b> )</b>
  </body>
</html>
</richcontent>
<node TEXT="&lt;year&gt;" STYLE_REF="klein und grau" ID="ID_1903736226" CREATED="1563016119883" MODIFIED="1563016119883"/>
<node TEXT="&lt;month&gt;" STYLE_REF="klein und grau" ID="ID_145504449" CREATED="1563016119883" MODIFIED="1563016119883"/>
<node TEXT="&lt;day&gt;" STYLE_REF="klein und grau" ID="ID_803118725" CREATED="1563016119883" MODIFIED="1563016119898"/>
<node TEXT="&lt;hour&gt;" STYLE_REF="klein und grau" ID="ID_727466043" CREATED="1563016119898" MODIFIED="1563016119898"/>
<node TEXT="&lt;minute&gt;" STYLE_REF="klein und grau" ID="ID_640094581" CREATED="1563016119898" MODIFIED="1563016119898"/>
<node TEXT="&lt;second&gt;" STYLE_REF="klein und grau" ID="ID_1627292625" CREATED="1563016119898" MODIFIED="1563016119898"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_329184412" CREATED="1563010597473" MODIFIED="1563010598984">
<node FOLDED="true" ID="ID_79232431" CREATED="1563010610353" MODIFIED="1611154006620" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">tuple </font><b>= ModificationDate</b>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1488540546" CREATED="1563010610353" MODIFIED="1563010610353">
<node TEXT="date and time (in local time system) when node was modified" ID="ID_411183847" CREATED="1563016020705" MODIFIED="1587362651161"/>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1805152017" CREATED="1563016079839" MODIFIED="1563016081519">
<node ID="ID_897494272" CREATED="1563016119867" MODIFIED="1563016119883"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <b>( </b><font color="#0000ff">&lt;year&gt;</font><b>, </b><font color="#0000ff">&lt;month&gt;</font><b>, </b><font color="#0000ff">&lt;day&gt;</font><b>, </b><font color="#0000ff">&lt;hour&gt;</font><b>, </b><font color="#0000ff">&lt;minute&gt;</font><b>, </b><font color="#0000ff">&lt;second&gt;</font><b> )</b>
  </body>
</html>
</richcontent>
<node TEXT="&lt;year&gt;" STYLE_REF="klein und grau" ID="ID_1978700062" CREATED="1563016119883" MODIFIED="1563016119883"/>
<node TEXT="&lt;month&gt;" STYLE_REF="klein und grau" ID="ID_102187002" CREATED="1563016119883" MODIFIED="1563016119883"/>
<node TEXT="&lt;day&gt;" STYLE_REF="klein und grau" ID="ID_487354899" CREATED="1563016119883" MODIFIED="1563016119898"/>
<node TEXT="&lt;hour&gt;" STYLE_REF="klein und grau" ID="ID_951766881" CREATED="1563016119898" MODIFIED="1563016119898"/>
<node TEXT="&lt;minute&gt;" STYLE_REF="klein und grau" ID="ID_1541981593" CREATED="1563016119898" MODIFIED="1563016119898"/>
<node TEXT="&lt;second&gt;" STYLE_REF="klein und grau" ID="ID_1406248290" CREATED="1563016119898" MODIFIED="1563016119898"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="..." STYLE_REF="klein und grau" ID="ID_424994756" CREATED="1563010537320" MODIFIED="1563010538979"/>
<node TEXT="attribute" STYLE_REF="klein und grau" ID="ID_788544690" CREATED="1510654921336" MODIFIED="1510766007348"/>
<node TEXT="." ID="ID_651192557" CREATED="1505561368013" MODIFIED="1505561368676">
<node FOLDED="true" ID="ID_102275272" CREATED="1505561368678" MODIFIED="1611154006620" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">dict</font>&#160;<b>= Attributes</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="code" STYLE_REF="klein und grau" ID="ID_1216165323" CREATED="1561899206519" MODIFIED="1561899211998">
<node TEXT="..." ID="ID_1290192095" CREATED="1561899195415" MODIFIED="1561899205096">
<node TEXT="&lt;&lt;" STYLE_REF="klein und grau" ID="ID_1621133687" CREATED="1561899191282" MODIFIED="1561899226137">
<node TEXT="=ID_705056167.text" ID="ID_1533823349" CREATED="1561899180064" MODIFIED="1561899180196" LINK="#ID_705056167">
<attribute NAME="use_node_for" VALUE="reference"/>
</node>
</node>
</node>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1731632379" CREATED="1510577789654" MODIFIED="1510577795846">
<node TEXT="dict of" ID="ID_1764833631" CREATED="1510655131141" MODIFIED="1510940184774">
<node TEXT="node&apos;s attribute" ID="ID_983909414" CREATED="1510940184776" MODIFIED="1510940191375"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_440309725" CREATED="1510940167001" MODIFIED="1510940168399">
<node ID="ID_706167875" CREATED="1510936896869" MODIFIED="1510940138330"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <b>{ </b><font color="#0000ff">[</font><b>&#160;</b><font color="#0000ff">&lt;key&gt;</font><b>: </b><font color="#0000ff">&lt;value&gt;</font><b>&#160;</b><font color="#0000ff">[</font><b>,</b><font color="#0000ff">] ]+</font><b>&#160;}</b>
  </body>
</html>
</richcontent>
<node TEXT="&lt;key&gt;" STYLE_REF="klein und grau" ID="ID_287044420" CREATED="1510936896885" MODIFIED="1541843461166" MIN_WIDTH="80">
<node TEXT="key of attribute" ID="ID_798429837" CREATED="1510654872543" MODIFIED="1510936919474"/>
</node>
<node TEXT="&lt;value&gt;" STYLE_REF="klein und grau" ID="ID_1877057381" CREATED="1510936896885" MODIFIED="1541843461166" MIN_WIDTH="80">
<node TEXT="value of attribute" ID="ID_1860020792" CREATED="1510936920463" MODIFIED="1510936923444"/>
</node>
</node>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_1613071904" CREATED="1562081146337" MODIFIED="1562081147618">
<node STYLE_REF="ANFORDERUNG (extern)" FOLDED="true" ID="ID_1033615264" CREATED="1562081212703" MODIFIED="1610868450879" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">string </font><b>= Attribute( </b><font color="#0000ff">&lt;attr&gt;</font><b> )</b>
  </body>
</html>
</richcontent>
<node TEXT="&lt;attr&gt;" STYLE_REF="klein und grau" ID="ID_1592505141" CREATED="1562081212715" MODIFIED="1562081212715"/>
<node TEXT="sets / returns" STYLE_REF="klein und grau" ID="ID_26505673" CREATED="1562081212715" MODIFIED="1562081219690"/>
</node>
</node>
<node TEXT="." ID="ID_1134406420" CREATED="1561010310732" MODIFIED="1561010311957">
<node ID="ID_930042614" CREATED="1561010357597" MODIFIED="1611154006621" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">None</font><b>&#160;= addAttribute( </b><font color="#0000ff">[ &lt;option&gt; [ </font><b>, </b><font color="#0000ff">] ]+</font><b>&#160;)</b>
  </body>
</html>
</richcontent>
<node TEXT="&lt;option&gt;" STYLE_REF="klein und grau" ID="ID_1427450222" CREATED="1561010404877" MODIFIED="1602271890296">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_290034551" CREATED="1561010530799" MODIFIED="1561010530799">
<node ID="ID_1184199374" CREATED="1561010527820" MODIFIED="1602271951697" MIN_WIDTH="160"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <b>key=</b><font color="#0000ff">&lt;string&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="&lt;string&gt;" STYLE_REF="klein und grau" ID="ID_1767208349" CREATED="1561010527820" MODIFIED="1561010541832" MIN_WIDTH="80">
<node TEXT="key of attribute" ID="ID_220253957" CREATED="1510654872543" MODIFIED="1510936919474"/>
</node>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_989231433" CREATED="1561010530799" MODIFIED="1561010530799">
<node ID="ID_809780173" CREATED="1561010527820" MODIFIED="1602271970490" MIN_WIDTH="160"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <b>value=</b><font color="#0000ff">&lt;string&gt;</font>
  </body>
</html>
</richcontent>
<node TEXT="&lt;string&gt;" STYLE_REF="klein und grau" ID="ID_976002578" CREATED="1561010527820" MODIFIED="1561010541832" MIN_WIDTH="80">
<node TEXT="value of attribute" ID="ID_191047854" CREATED="1510936920463" MODIFIED="1510936923444"/>
</node>
</node>
</node>
</node>
<node TEXT="code" STYLE_REF="klein und grau" ID="ID_579599477" CREATED="1602304080421" MODIFIED="1602304083054">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_127969761" CREATED="1602304083055" MODIFIED="1602304085492">
<node TEXT="create new attribute within node" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1069123574" CREATED="1602304085496" MODIFIED="1602304098372">
<node TEXT="&gt;&gt;" STYLE_REF="klein und grau" ID="ID_1074434199" CREATED="1602304248754" MODIFIED="1602304250703">
<node TEXT="=ID_705056167.text" ID="ID_361417027" CREATED="1602304237135" MODIFIED="1602304289250" LINK="#ID_705056167">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="80" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_256259891" STARTINCLINATION="1061;0;" ENDINCLINATION="1061;0;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<attribute NAME="use_node_for" VALUE="activation"/>
<node TEXT="append ATTRIBUTE node" STYLE_REF="klein und grau" ID="ID_833241339" CREATED="1602304252152" MODIFIED="1602304265408"/>
</node>
</node>
</node>
</node>
</node>
</node>
</node>
<node TEXT="style" STYLE_REF="klein und grau" ID="ID_71185967" CREATED="1510766000918" MODIFIED="1510766005394"/>
<node TEXT="." ID="ID_339705965" CREATED="1505561368013" MODIFIED="1505561368676">
<node ID="ID_372119708" CREATED="1505561368678" MODIFIED="1611154006621" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">string</font>&#160;<b>= Style</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="sets / returns" STYLE_REF="klein und grau" ID="ID_189358777" CREATED="1510577789654" MODIFIED="1610868530072">
<node TEXT="style name string set for node object" ID="ID_966284235" CREATED="1510655131141" MODIFIED="1610790340781"/>
</node>
</node>
</node>
<node TEXT="." ID="ID_1370859049" CREATED="1610790351098" MODIFIED="1610790353479">
<node STYLE_REF="ANFORDERUNG (extern)" ID="ID_1089384415" CREATED="1610790353481" MODIFIED="1610868450879" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">bool </font><b>= setStyle()</b>
  </body>
</html>
</richcontent>
<node TEXT="scope" STYLE_REF="klein und grau" ID="ID_529868676" CREATED="1610790401324" MODIFIED="1610790403419">
<node TEXT="assign a style name with node object" ID="ID_177081297" CREATED="1610790404603" MODIFIED="1610790414989"/>
</node>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_580023412" CREATED="1610790417443" MODIFIED="1610790420883">
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1577972848" CREATED="1610790468201" MODIFIED="1610790468203">
<node TEXT="True" ID="ID_74518240" CREATED="1610790420885" MODIFIED="1610790466750">
<font BOLD="true"/>
<node TEXT="when valid style was found and assigned" STYLE_REF="klein und grau" ID="ID_625208918" CREATED="1610790428864" MODIFIED="1610790465527"/>
</node>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1374716843" CREATED="1610790468209" MODIFIED="1610790468210">
<node TEXT="False" ID="ID_1342281609" CREATED="1610790442750" MODIFIED="1610790467166">
<font BOLD="true"/>
<node TEXT="if requested style name does not exist" STYLE_REF="klein und grau" ID="ID_613469948" CREATED="1610790444819" MODIFIED="1610790465313"/>
</node>
</node>
</node>
</node>
</node>
<node TEXT="details" STYLE_REF="klein und grau" ID="ID_394590732" CREATED="1561892425365" MODIFIED="1561892427259"/>
<node TEXT="." ID="ID_1398482981" CREATED="1561892430783" MODIFIED="1561892432189">
<node FOLDED="true" ID="ID_205404970" CREATED="1561892442081" MODIFIED="1611154006621" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">string </font><b>= Details</b>
  </body>
</html>
</richcontent>
<node TEXT="sets / returns" STYLE_REF="klein und grau" ID="ID_1831579040" CREATED="1561892442081" MODIFIED="1602315605076">
<node TEXT="details plain text portion" ID="ID_1842291466" CREATED="1602315606132" MODIFIED="1602315637343">
<node TEXT="without html structure" STYLE_REF="klein und grau" ID="ID_1510222970" CREATED="1602315637950" MODIFIED="1602315644553"/>
</node>
</node>
</node>
</node>
<node TEXT="..." STYLE_REF="klein und grau" ID="ID_170193021" CREATED="1561892428038" MODIFIED="1561892429697"/>
<node TEXT="link" STYLE_REF="klein und grau" ID="ID_1014148620" CREATED="1510766919610" MODIFIED="1510766921442"/>
<node TEXT="." ID="ID_635633662" CREATED="1505561368013" MODIFIED="1505561368676">
<node FOLDED="true" ID="ID_1708250778" CREATED="1505561368678" MODIFIED="1611154006621" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">string</font>&#160;<b>= CoreLink</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1671106790" CREATED="1510577789654" MODIFIED="1510577795846">
<node TEXT="first node ID referenced within core" ID="ID_651864720" CREATED="1510766984741" MODIFIED="1510767089673"/>
</node>
</node>
</node>
<node TEXT="." ID="ID_67934096" CREATED="1505561368013" MODIFIED="1505561368676">
<node ID="ID_1399631778" CREATED="1505561368678" MODIFIED="1611154006621" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#0000ff">string</font>&#160;<b>= Link</b>
    </p>
  </body>
</html>
</richcontent>
<node TEXT="sets / returns" STYLE_REF="klein und grau" ID="ID_1688340471" CREATED="1510577789654" MODIFIED="1561840455180">
<node TEXT="complete hyperlink string of node" ID="ID_1745775954" CREATED="1561840456477" MODIFIED="1610790547576"/>
</node>
</node>
</node>
<node TEXT="icon" STYLE_REF="klein und grau" ID="ID_1130852388" CREATED="1505562017185" MODIFIED="1510766924534"/>
<node TEXT="." ID="ID_453091900" CREATED="1562075260587" MODIFIED="1562075261308">
<node FOLDED="true" ID="ID_1143525698" CREATED="1562075269548" MODIFIED="1611154006621" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">list </font><b>= Icons</b>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1727850033" CREATED="1562075269560" MODIFIED="1562075269560">
<node TEXT="list of" ID="ID_1444924401" CREATED="1562075277228" MODIFIED="1562075279980">
<node TEXT="icon identification string" ID="ID_506013718" CREATED="1562075279984" MODIFIED="1562075285477"/>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_97527352" CREATED="1562075431515" MODIFIED="1562077673295">
<node FOLDED="true" ID="ID_896433886" CREATED="1562075489302" MODIFIED="1611154006621" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">None </font><b>= addIcon( </b><font color="#0000ff">&lt;string&gt;</font><b>&#160;)</b>
  </body>
</html>
</richcontent>
<node TEXT="&lt;string&gt;" STYLE_REF="klein und grau" ID="ID_1954874858" CREATED="1562075506955" MODIFIED="1562075527891">
<node TEXT="icon identification string" ID="ID_1399882203" CREATED="1562075508798" MODIFIED="1562075537268">
<node TEXT="to be created" STYLE_REF="klein und grau" ID="ID_1399069942" CREATED="1562075542428" MODIFIED="1562075546396"/>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_1976829015" CREATED="1562075431515" MODIFIED="1562077673295">
<node FOLDED="true" ID="ID_764271018" CREATED="1562075489302" MODIFIED="1611154006622" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">None </font><b>= delIcon( </b><font color="#0000ff">&lt;string&gt;</font><b>&#160;)</b>
  </body>
</html>
</richcontent>
<node TEXT="&lt;string&gt;" STYLE_REF="klein und grau" ID="ID_1065365941" CREATED="1562075506955" MODIFIED="1562075527891">
<node TEXT="icon identification string" ID="ID_460600781" CREATED="1562075508798" MODIFIED="1562075537268">
<node TEXT="to be deleted" STYLE_REF="klein und grau" ID="ID_332770523" CREATED="1562075542428" MODIFIED="1562077688503"/>
</node>
</node>
</node>
</node>
<node TEXT="." ID="ID_1011418421" CREATED="1505561970245" MODIFIED="1505561970808">
<node STYLE_REF="ANFORDERUNG (extern)" FOLDED="true" ID="ID_155452813" CREATED="1505558148711" MODIFIED="1610868450879" MIN_WIDTH="320"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">bool </font><b>= isChecked()</b>
  </body>
</html>
</richcontent>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_484352681" CREATED="1505558148711" MODIFIED="1505558148711"/>
</node>
</node>
</node>
</node>
<node TEXT="..." ID="ID_1425496340" CREATED="1510398279995" MODIFIED="1510398280917"/>
<node TEXT="[ fct ]" STYLE_REF="klein und grau" ID="ID_560882102" CREATED="1510562970686" MODIFIED="1583832904161" MIN_WIDTH="60">
<node ID="ID_806082309" CREATED="1610696949401" MODIFIED="1610697420849" MIN_WIDTH="360"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">string </font><b>= get_version_specific_file_encoding()</b>
  </body>
</html>
</richcontent>
<node TEXT="act" STYLE_REF="klein und grau" ID="ID_750463592" CREATED="1610697530585" MODIFIED="1610697950471" MIN_WIDTH="60"/>
<node TEXT="&lt;" STYLE_REF="klein und grau" ID="ID_1893806815" CREATED="1610697934911" MODIFIED="1610697950471" MIN_WIDTH="60">
<node TEXT="version" ID="ID_1774772976" CREATED="1610697941094" MODIFIED="1610697942479"/>
</node>
<node TEXT="code" STYLE_REF="klein und grau" ID="ID_286573509" CREATED="1610697947043" MODIFIED="1610697950471" MIN_WIDTH="60"/>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_217050708" CREATED="1610697386400" MODIFIED="1610697950472" MIN_WIDTH="60">
<node TEXT="encoding respective to file version" ID="ID_1158266866" CREATED="1610697918960" MODIFIED="1610697929444"/>
</node>
</node>
<node TEXT="getCoreTextFromNode()" ID="ID_408460964" CREATED="1510562929310" MODIFIED="1610697420851" MIN_WIDTH="360">
<node TEXT="act" STYLE_REF="klein und grau" ID="ID_1619020964" CREATED="1510563005131" MODIFIED="1510563005131"/>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_1074960839" CREATED="1510556976344" MODIFIED="1510556977532">
<node TEXT="get TEXT attribute of node if present" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_196729060" CREATED="1510556977959" MODIFIED="1510556979676"/>
</node>
<node TEXT="." STYLE_REF="klein und grau" ID="ID_466251694" CREATED="1510557031656" MODIFIED="1510557032583">
<node TEXT="strip text from RICHTEXT content if present" STYLE_REF="POSITIV (gr&#xfc;n)" ID="ID_1440366436" CREATED="1510557032953" MODIFIED="1510557722354"/>
</node>
</node>
<node ID="ID_838144026" CREATED="1561911184531" MODIFIED="1610697420851" MIN_WIDTH="360"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <font color="#0000ff">list </font><b>= reduce_node_list()</b>
  </body>
</html>
</richcontent>
<node TEXT="act" STYLE_REF="klein und grau" ID="ID_330698355" CREATED="1561911677046" MODIFIED="1561911677046"/>
<node TEXT="returns" STYLE_REF="klein und grau" ID="ID_1314709020" CREATED="1561911184531" MODIFIED="1561911184548"/>
</node>
</node>
</node>
</node>
<node TEXT="FILESYSTEM" STYLE_REF="klein und grau" POSITION="right" ID="ID_1349007524" CREATED="1438513086187" MODIFIED="1608708066490" MIN_WIDTH="80">
<node ID="ID_786976233" CREATED="1438513104828" MODIFIED="1438513157171"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      [ <font color="#0000ff">&lt;project_folder&gt;</font>&#160;]
    </p>
  </body>
</html>
</richcontent>
<node TEXT="/" ID="ID_342567236" CREATED="1438513101156" MODIFIED="1438513103593">
<node TEXT="..." ID="ID_554950962" CREATED="1438513069453" MODIFIED="1505557521324">
<node TEXT="SYNTAX" STYLE_REF="klein und grau" ID="ID_533525634" CREATED="1438513301218" MODIFIED="1438513303656"/>
</node>
</node>
</node>
</node>
<node TEXT="docu" STYLE_REF="klein und grau" POSITION="left" ID="ID_784078348" CREATED="1426347656103" MODIFIED="1552467114786" MIN_WIDTH="80">
<node TEXT="[ EDITOR ]" STYLE_REF="klein und grau" ID="ID_478924010" CREATED="1461574234950" MODIFIED="1461574239583">
<node TEXT="c:/Program Files (x86)/Vim/vim74/gvim" ID="ID_1998981292" CREATED="1426347673163" MODIFIED="1504877592818">
<attribute_layout NAME_WIDTH="74" VALUE_WIDTH="236"/>
<attribute NAME="type" VALUE="EditorSpecification"/>
</node>
</node>
<node TEXT="[ EDITOR ]" STYLE_REF="klein und grau" ID="ID_1839340279" CREATED="1461574234950" MODIFIED="1461574239583">
<node TEXT="c:\PROGS\Vim\vim74" ID="ID_555298023" CREATED="1426347673163" MODIFIED="1505569246919">
<attribute_layout NAME_WIDTH="74" VALUE_WIDTH="236"/>
<attribute NAME="type" VALUE="EditorSpecification"/>
</node>
</node>
</node>
</node>
</map>
