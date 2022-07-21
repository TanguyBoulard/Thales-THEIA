<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="17008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="NI.SortType" Type="Int">3</Property>
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="VIs" Type="Folder">
			<Item Name="Multi U-Link DAQ Continuous value.vi" Type="VI" URL="../VIs/Multi U-Link DAQ Continuous value.vi"/>
			<Item Name="Multi U-Link DAQ Single value.vi" Type="VI" URL="../VIs/Multi U-Link DAQ Single value.vi"/>
		</Item>
		<Item Name="SubVIs" Type="Folder">
			<Item Name="Initialization (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Initialization (SubVI).vi"/>
			<Item Name="Port Close (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Port Close (SubVI).vi"/>
			<Item Name="Port Flush (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Port Flush (SubVI).vi"/>
			<Item Name="Port Open (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Port Open (SubVI).vi"/>
			<Item Name="Port Read (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Port Read (SubVI).vi"/>
			<Item Name="Port Write (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Port Write (SubVI).vi"/>
			<Item Name="Set Multiplier (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Set Multiplier (SubVI).vi"/>
			<Item Name="Set Offset (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Set Offset (SubVI).vi"/>
			<Item Name="Set Scale (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Set Scale (SubVI).vi"/>
			<Item Name="Set Trigger Level (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Set Trigger Level (SubVI).vi"/>
			<Item Name="Set Wavelength (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Set Wavelength (SubVI).vi"/>
			<Item Name="Wait (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Wait (SubVI).vi"/>
			<Item Name="Send Continuous Value (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Send Continuous Value (SubVI).vi"/>
			<Item Name="Stop Continuous Value (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Stop Continuous Value (SubVI).vi"/>
			<Item Name="Create File (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Create File (SubVI).vi"/>
			<Item Name="Read Config File (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Read Config File (SubVI).vi"/>
			<Item Name="Write User File (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Write User File (SubVI).vi"/>
			<Item Name="Check Sections and Parameters (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Check Sections and Parameters (SubVI).vi"/>
			<Item Name="New Data (SubVI).vi" Type="VI" URL="../VIs/SubVIs/New Data (SubVI).vi"/>
			<Item Name="Read Continuous Value (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Read Continuous Value (SubVI).vi"/>
			<Item Name="Read Single Value (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Read Single Value (SubVI).vi"/>
		</Item>
		<Item Name="Type Def" Type="Folder">
			<Item Name="Data.ctl" Type="VI" URL="../VIs/Type Def/Data.ctl"/>
		</Item>
		<Item Name="Icons" Type="Folder">
			<Item Name="exe.ico" Type="Document" URL="../Icons/exe.ico"/>
		</Item>
		<Item Name="Config" Type="Folder">
			<Item Name="User.ini" Type="Document" URL="../Config/User.ini"/>
		</Item>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Application Directory.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Application Directory.vi"/>
				<Item Name="BuildHelpPath.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/BuildHelpPath.vi"/>
				<Item Name="Check if File or Folder Exists.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Check if File or Folder Exists.vi"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Details Display Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Details Display Dialog.vi"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
				<Item Name="ErrWarn.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/ErrWarn.ctl"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="Find Tag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find Tag.vi"/>
				<Item Name="Format Message String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Format Message String.vi"/>
				<Item Name="General Error Handler Core CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler Core CORE.vi"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="GetHelpDir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetHelpDir.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="NI_PackedLibraryUtility.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/LVLibp/NI_PackedLibraryUtility.lvlib"/>
				<Item Name="Not Found Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Not Found Dialog.vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="Set Bold Text.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set Bold Text.vi"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="Simple Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Simple Error Handler.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="VISA Configure Serial Port" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port"/>
				<Item Name="VISA Configure Serial Port (Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Instr).vi"/>
				<Item Name="VISA Configure Serial Port (Serial Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Serial Instr).vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="LVBoundsTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVBoundsTypeDef.ctl"/>
				<Item Name="Get String Text Bounds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Get String Text Bounds.vi"/>
				<Item Name="Get Text Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Get Text Rect.vi"/>
				<Item Name="Convert property node font to graphics font.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Convert property node font to graphics font.vi"/>
				<Item Name="Longest Line Length in Pixels.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Longest Line Length in Pixels.vi"/>
				<Item Name="LVRectTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVRectTypeDef.ctl"/>
				<Item Name="Three Button Dialog CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog CORE.vi"/>
				<Item Name="Three Button Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog.vi"/>
				<Item Name="NI_AALBase.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALBase.lvlib"/>
				<Item Name="NI_LVConfig.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/config.llb/NI_LVConfig.lvlib"/>
				<Item Name="8.6CompatibleGlobalVar.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/config.llb/8.6CompatibleGlobalVar.vi"/>
				<Item Name="Space Constant.vi" Type="VI" URL="/&lt;vilib&gt;/dlg_ctls.llb/Space Constant.vi"/>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="Multi U-Link DAQ Continuous value" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{857230DA-61A4-49BA-9C1D-6668EAA273FC}</Property>
				<Property Name="App_INI_GUID" Type="Str">{71BF10F0-0292-4B78-B063-C10AE69393CA}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{81A48C5E-1CFA-4152-B968-6FAB5CD95B0E}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">Multi U-Link DAQ Continuous value</Property>
				<Property Name="Bld_defaultLanguage" Type="Str">French</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">/G/My Drive/Scolarité/INSA/5-GP/Stage Thales/Projet/Software/builds/Multi U-Link DAQ Continuous value</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{5B85CCB2-644E-46CB-AB9A-1FE990BB7463}</Property>
				<Property Name="Bld_version.build" Type="Int">6</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">Multi U-Link DAQ Continuous value.exe</Property>
				<Property Name="Destination[0].path" Type="Path">/G/My Drive/Scolarité/INSA/5-GP/Stage Thales/Projet/Software/builds/Multi U-Link DAQ Continuous value/Multi U-Link DAQ Continuous value.exe</Property>
				<Property Name="Destination[0].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Répertoire de support</Property>
				<Property Name="Destination[1].path" Type="Path">/G/My Drive/Scolarité/INSA/5-GP/Stage Thales/Projet/Software/builds/Multi U-Link DAQ Continuous value/data</Property>
				<Property Name="Destination[1].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="Destination[2].destName" Type="Str">Config</Property>
				<Property Name="Destination[2].path" Type="Path">/G/My Drive/Scolarité/INSA/5-GP/Stage Thales/Projet/Software/builds/Multi U-Link DAQ Continuous value/Config</Property>
				<Property Name="Destination[2].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="Destination[3].destName" Type="Str">Icons</Property>
				<Property Name="Destination[3].path" Type="Path">/G/My Drive/Scolarité/INSA/5-GP/Stage Thales/Projet/Software/builds/Multi U-Link DAQ Continuous value/Icons</Property>
				<Property Name="Destination[3].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="DestinationCount" Type="Int">4</Property>
				<Property Name="Exe_iconItemID" Type="Ref">/My Computer/Icons/exe.ico</Property>
				<Property Name="Source[0].itemID" Type="Str">{FA9D4792-3048-4F44-BCDD-A99A637AE3DA}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/VIs/Multi U-Link DAQ Continuous value.vi</Property>
				<Property Name="Source[1].properties[0].type" Type="Str">Show menu bar</Property>
				<Property Name="Source[1].properties[0].value" Type="Bool">false</Property>
				<Property Name="Source[1].properties[1].type" Type="Str">Show vertical scroll bar</Property>
				<Property Name="Source[1].properties[1].value" Type="Bool">false</Property>
				<Property Name="Source[1].properties[2].type" Type="Str">Show toolbar</Property>
				<Property Name="Source[1].properties[2].value" Type="Bool">false</Property>
				<Property Name="Source[1].properties[3].type" Type="Str">Show Abort button</Property>
				<Property Name="Source[1].properties[3].value" Type="Bool">false</Property>
				<Property Name="Source[1].propertiesCount" Type="Int">4</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="Source[2].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[2].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[2].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[2].itemID" Type="Ref">/My Computer/SubVIs</Property>
				<Property Name="Source[2].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[2].type" Type="Str">Container</Property>
				<Property Name="Source[3].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[3].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[3].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[3].itemID" Type="Ref">/My Computer/Type Def</Property>
				<Property Name="Source[3].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[3].type" Type="Str">Container</Property>
				<Property Name="Source[4].Container.applyDestination" Type="Bool">true</Property>
				<Property Name="Source[4].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[4].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[4].destinationIndex" Type="Int">3</Property>
				<Property Name="Source[4].itemID" Type="Ref">/My Computer/Icons</Property>
				<Property Name="Source[4].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[4].type" Type="Str">Container</Property>
				<Property Name="Source[5].Container.applyDestination" Type="Bool">true</Property>
				<Property Name="Source[5].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[5].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[5].destinationIndex" Type="Int">2</Property>
				<Property Name="Source[5].itemID" Type="Ref">/My Computer/Config</Property>
				<Property Name="Source[5].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[5].type" Type="Str">Container</Property>
				<Property Name="SourceCount" Type="Int">6</Property>
				<Property Name="TgtF_companyName" Type="Str">THALES LAS FRANCE</Property>
				<Property Name="TgtF_fileDescription" Type="Str">Multi U-Link DAQ Continuous value</Property>
				<Property Name="TgtF_internalName" Type="Str">Multi U-Link DAQ Continuous value</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2022 THALES LAS FRANCE</Property>
				<Property Name="TgtF_productName" Type="Str">Multi U-Link DAQ Continuous value</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{FAFBA458-1433-473B-BFA1-4D7736DAB27F}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">Multi U-Link DAQ Continuous value.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
			<Item Name="Multi U-Link DAQ Single value" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{4574A0AC-F52F-4E28-99F1-C81FAD4A511B}</Property>
				<Property Name="App_INI_GUID" Type="Str">{26BAA22C-E7AD-467A-B6E1-8C6CC7282018}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{B7C816D1-D7AA-4315-BEEC-0450FCCB8020}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">Multi U-Link DAQ Single value</Property>
				<Property Name="Bld_defaultLanguage" Type="Str">French</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">/G/My Drive/Scolarité/INSA/5-GP/Stage Thales/Projet/Software/builds/Multi U-Link DAQ Single value</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{F7687A42-80B7-4997-A1FB-CFF0E8BC6A41}</Property>
				<Property Name="Bld_version.build" Type="Int">6</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">Multi U-Link DAQ Single value.exe</Property>
				<Property Name="Destination[0].path" Type="Path">/G/My Drive/Scolarité/INSA/5-GP/Stage Thales/Projet/Software/builds/Multi U-Link DAQ Single value/Multi U-Link DAQ Single value.exe</Property>
				<Property Name="Destination[0].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Répertoire de support</Property>
				<Property Name="Destination[1].path" Type="Path">/G/My Drive/Scolarité/INSA/5-GP/Stage Thales/Projet/Software/builds/Multi U-Link DAQ Single value/data</Property>
				<Property Name="Destination[1].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="Destination[2].destName" Type="Str">Conifg</Property>
				<Property Name="Destination[2].path" Type="Path">/G/My Drive/Scolarité/INSA/5-GP/Stage Thales/Projet/Software/builds/Multi U-Link DAQ Single value/Conifg</Property>
				<Property Name="Destination[2].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="Destination[3].destName" Type="Str">Icons</Property>
				<Property Name="Destination[3].path" Type="Path">/G/My Drive/Scolarité/INSA/5-GP/Stage Thales/Projet/Software/builds/Multi U-Link DAQ Single value/Icons</Property>
				<Property Name="Destination[3].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="DestinationCount" Type="Int">4</Property>
				<Property Name="Exe_iconItemID" Type="Ref">/My Computer/Icons/exe.ico</Property>
				<Property Name="Source[0].itemID" Type="Str">{FA9D4792-3048-4F44-BCDD-A99A637AE3DA}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/VIs/Multi U-Link DAQ Single value.vi</Property>
				<Property Name="Source[1].properties[0].type" Type="Str">Show menu bar</Property>
				<Property Name="Source[1].properties[0].value" Type="Bool">false</Property>
				<Property Name="Source[1].properties[1].type" Type="Str">Show vertical scroll bar</Property>
				<Property Name="Source[1].properties[1].value" Type="Bool">false</Property>
				<Property Name="Source[1].properties[2].type" Type="Str">Show toolbar</Property>
				<Property Name="Source[1].properties[2].value" Type="Bool">false</Property>
				<Property Name="Source[1].properties[3].type" Type="Str">Show Abort button</Property>
				<Property Name="Source[1].properties[3].value" Type="Bool">false</Property>
				<Property Name="Source[1].propertiesCount" Type="Int">4</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="Source[2].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[2].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[2].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[2].itemID" Type="Ref">/My Computer/SubVIs</Property>
				<Property Name="Source[2].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[2].type" Type="Str">Container</Property>
				<Property Name="Source[3].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[3].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[3].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[3].itemID" Type="Ref">/My Computer/Type Def</Property>
				<Property Name="Source[3].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[3].type" Type="Str">Container</Property>
				<Property Name="Source[4].Container.applyDestination" Type="Bool">true</Property>
				<Property Name="Source[4].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[4].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[4].destinationIndex" Type="Int">3</Property>
				<Property Name="Source[4].itemID" Type="Ref">/My Computer/Icons</Property>
				<Property Name="Source[4].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[4].type" Type="Str">Container</Property>
				<Property Name="Source[5].Container.applyDestination" Type="Bool">true</Property>
				<Property Name="Source[5].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[5].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[5].destinationIndex" Type="Int">2</Property>
				<Property Name="Source[5].itemID" Type="Ref">/My Computer/Config</Property>
				<Property Name="Source[5].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[5].type" Type="Str">Container</Property>
				<Property Name="SourceCount" Type="Int">6</Property>
				<Property Name="TgtF_companyName" Type="Str">THALES LAS FRANCE</Property>
				<Property Name="TgtF_fileDescription" Type="Str">Multi U-Link DAQ Single value</Property>
				<Property Name="TgtF_internalName" Type="Str">Multi U-Link DAQ Single value</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2022 THALES LAS FRANCE</Property>
				<Property Name="TgtF_productName" Type="Str">Multi U-Link DAQ Single value</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{1F40E498-5109-4818-8C9F-59BD1947AF87}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">Multi U-Link DAQ Single value.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
		</Item>
	</Item>
</Project>
