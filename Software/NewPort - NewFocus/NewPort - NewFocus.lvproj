<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="17008000">
	<Item Name="Poste de travail" Type="My Computer">
		<Property Name="NI.SortType" Type="Int">3</Property>
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">Poste de travail/VI Serveur</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">Poste de travail/VI Serveur</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="VIs" Type="Folder">
			<Item Name="New Focus - rétroaction.vi" Type="VI" URL="../VIs/New Focus - rétroaction.vi"/>
		</Item>
		<Item Name="SubVIs" Type="Folder">
			<Item Name="Set Zero Position (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Set Zero Position (SubVI).vi"/>
			<Item Name="Init Multiple Devices (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Init Multiple Devices (SubVI).vi"/>
			<Item Name="Get Master Device Adress (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Get Master Device Adress (SubVI).vi"/>
			<Item Name="Abort Motion (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Abort Motion (SubVI).vi"/>
			<Item Name="Close (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Close (SubVI).vi"/>
			<Item Name="Device Close (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Device Close (SubVI).vi"/>
			<Item Name="Device open (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Device open (SubVI).vi"/>
			<Item Name="Get Device Adresses (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Get Device Adresses (SubVI).vi"/>
			<Item Name="Get Model Serial (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Get Model Serial (SubVI).vi"/>
			<Item Name="Get Motion Done (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Get Motion Done (SubVI).vi"/>
			<Item Name="On Stop Motion (SubVI).vi" Type="VI" URL="../VIs/SubVIs/On Stop Motion (SubVI).vi"/>
			<Item Name="Set Controller Name (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Set Controller Name (SubVI).vi"/>
			<Item Name="Shutdown (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Shutdown (SubVI).vi"/>
			<Item Name="Initialize Devices (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Initialize Devices (SubVI).vi"/>
			<Item Name="Get Discovered Devices (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Get Discovered Devices (SubVI).vi"/>
			<Item Name="On Device Selected (SubVI).vi" Type="VI" URL="../VIs/SubVIs/On Device Selected (SubVI).vi"/>
			<Item Name="Relative Move (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Relative Move (SubVI).vi"/>
			<Item Name="On Go (SubVI).vi" Type="VI" URL="../VIs/SubVIs/On Go (SubVI).vi"/>
			<Item Name="Load Config File (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Load Config File (SubVI).vi"/>
			<Item Name="Config File (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Config File (SubVI).vi"/>
			<Item Name="Theta(Transmission) (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Theta(Transmission) (SubVI).vi"/>
			<Item Name="Transmission(Theta) (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Transmission(Theta) (SubVI).vi"/>
			<Item Name="Get Position (SubVI).vi" Type="VI" URL="../VIs/SubVIs/Get Position (SubVI).vi"/>
		</Item>
		<Item Name="Type Def" Type="Folder">
			<Item Name="Data cluster.ctl" Type="VI" URL="../VIs/Type Def/Data cluster.ctl"/>
		</Item>
		<Item Name="Icons" Type="Folder">
			<Item Name="exe.ico" Type="Document" URL="../Icons/exe.ico"/>
		</Item>
		<Item Name="dll" Type="Folder">
			<Item Name="CmdLib.dll" Type="Document" URL="../dll/CmdLib.dll"/>
			<Item Name="CmdLib8742.dll" Type="Document" URL="../dll/CmdLib8742.dll"/>
			<Item Name="DeviceIOLib.dll" Type="Document" URL="../dll/DeviceIOLib.dll"/>
			<Item Name="NpEthernet.dll" Type="Document" URL="../dll/NpEthernet.dll"/>
			<Item Name="NpSerial.dll" Type="Document" URL="../dll/NpSerial.dll"/>
			<Item Name="UsbDllWrap.dll" Type="Document" URL="../dll/UsbDllWrap.dll"/>
		</Item>
		<Item Name="Config" Type="Folder">
			<Item Name="User.ini" Type="Document" URL="../Config/User.ini"/>
		</Item>
		<Item Name="Dépendances" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Check if File or Folder Exists.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Check if File or Folder Exists.vi"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="NI_PackedLibraryUtility.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/LVLibp/NI_PackedLibraryUtility.lvlib"/>
				<Item Name="NI_LVConfig.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/config.llb/NI_LVConfig.lvlib"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="8.6CompatibleGlobalVar.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/config.llb/8.6CompatibleGlobalVar.vi"/>
				<Item Name="Simple Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Simple Error Handler.vi"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="General Error Handler Core CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler Core CORE.vi"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
				<Item Name="Format Message String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Format Message String.vi"/>
				<Item Name="Set Bold Text.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set Bold Text.vi"/>
				<Item Name="Find Tag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find Tag.vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="Details Display Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Details Display Dialog.vi"/>
				<Item Name="ErrWarn.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/ErrWarn.ctl"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="Not Found Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Not Found Dialog.vi"/>
				<Item Name="Three Button Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog.vi"/>
				<Item Name="Three Button Dialog CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog CORE.vi"/>
				<Item Name="LVRectTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVRectTypeDef.ctl"/>
				<Item Name="Longest Line Length in Pixels.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Longest Line Length in Pixels.vi"/>
				<Item Name="Convert property node font to graphics font.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Convert property node font to graphics font.vi"/>
				<Item Name="Get Text Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Get Text Rect.vi"/>
				<Item Name="Get String Text Bounds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Get String Text Bounds.vi"/>
				<Item Name="LVBoundsTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVBoundsTypeDef.ctl"/>
				<Item Name="BuildHelpPath.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/BuildHelpPath.vi"/>
				<Item Name="GetHelpDir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetHelpDir.vi"/>
			</Item>
			<Item Name="Port Write (SubVI).vi" Type="VI" URL="/C/Users/thales/Desktop/Gentec-EO PID/U-Link/VIs/SubVIs/Port Write (SubVI).vi"/>
			<Item Name="Port Read (SubVI).vi" Type="VI" URL="/C/Users/thales/Desktop/Gentec-EO PID/U-Link/VIs/SubVIs/Port Read (SubVI).vi"/>
			<Item Name="Wait (SubVI).vi" Type="VI" URL="/C/Users/thales/Desktop/Gentec-EO PID/U-Link/VIs/SubVIs/Wait (SubVI).vi"/>
			<Item Name="Set Scale (SubVI).vi" Type="VI" URL="/C/Users/thales/Desktop/Gentec-EO PID/U-Link/VIs/SubVIs/Set Scale (SubVI).vi"/>
			<Item Name="Set Wavelength (SubVI).vi" Type="VI" URL="/C/Users/thales/Desktop/Gentec-EO PID/U-Link/VIs/SubVIs/Set Wavelength (SubVI).vi"/>
			<Item Name="Set Offset (SubVI).vi" Type="VI" URL="/C/Users/thales/Desktop/Gentec-EO PID/U-Link/VIs/SubVIs/Set Offset (SubVI).vi"/>
			<Item Name="Set Multiplier (SubVI).vi" Type="VI" URL="/C/Users/thales/Desktop/Gentec-EO PID/U-Link/VIs/SubVIs/Set Multiplier (SubVI).vi"/>
			<Item Name="Set Trigger Level (SubVI).vi" Type="VI" URL="/C/Users/thales/Desktop/Gentec-EO PID/U-Link/VIs/SubVIs/Set Trigger Level (SubVI).vi"/>
			<Item Name="Initialization (SubVI).vi" Type="VI" URL="/C/Users/thales/Desktop/Gentec-EO PID/U-Link/VIs/SubVIs/Initialization (SubVI).vi"/>
		</Item>
		<Item Name="Spécifications de construction" Type="Build">
			<Item Name="New Focus" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{25B50FC1-88F4-4420-ADB4-B398BC966C8E}</Property>
				<Property Name="App_INI_GUID" Type="Str">{56D46FAD-ECA4-47B7-B32D-F293558D9821}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{F67DF10F-1649-40D2-9E16-745DC41B963B}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">New Focus</Property>
				<Property Name="Bld_defaultLanguage" Type="Str">French</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/New Focus</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{35AA8DA7-E469-4B0D-86E7-4AA7E0AE296D}</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">New Focus.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/New Focus/New Focus.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Répertoire de support</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/New Focus/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Exe_iconItemID" Type="Ref">/Poste de travail/Icons/exe.ico</Property>
				<Property Name="Source[0].itemID" Type="Str">{48671DAF-391A-43BE-B7FC-98D4373F4C32}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/Poste de travail/VIs/New Focus - rétroaction.vi</Property>
				<Property Name="Source[1].newName" Type="Str">main.vi</Property>
				<Property Name="Source[1].properties[0].type" Type="Str">Window has title bar</Property>
				<Property Name="Source[1].properties[0].value" Type="Bool">true</Property>
				<Property Name="Source[1].properties[1].type" Type="Str">Show menu bar</Property>
				<Property Name="Source[1].properties[1].value" Type="Bool">false</Property>
				<Property Name="Source[1].properties[10].type" Type="Str">Allow debugging</Property>
				<Property Name="Source[1].properties[10].value" Type="Bool">true</Property>
				<Property Name="Source[1].properties[2].type" Type="Str">Show vertical scroll bar</Property>
				<Property Name="Source[1].properties[2].value" Type="Bool">false</Property>
				<Property Name="Source[1].properties[3].type" Type="Str">Show horizontal scroll bar</Property>
				<Property Name="Source[1].properties[3].value" Type="Bool">false</Property>
				<Property Name="Source[1].properties[4].type" Type="Str">Show toolbar</Property>
				<Property Name="Source[1].properties[4].value" Type="Bool">false</Property>
				<Property Name="Source[1].properties[5].type" Type="Str">Show fp when called</Property>
				<Property Name="Source[1].properties[5].value" Type="Bool">false</Property>
				<Property Name="Source[1].properties[6].type" Type="Str">Show Abort button</Property>
				<Property Name="Source[1].properties[6].value" Type="Bool">true</Property>
				<Property Name="Source[1].properties[7].type" Type="Str">Window behavior</Property>
				<Property Name="Source[1].properties[7].value" Type="Str">Default</Property>
				<Property Name="Source[1].properties[8].type" Type="Str">Window run-time position</Property>
				<Property Name="Source[1].properties[8].value" Type="Str">Centered</Property>
				<Property Name="Source[1].properties[9].type" Type="Str">Allow user to close window</Property>
				<Property Name="Source[1].properties[9].value" Type="Bool">true</Property>
				<Property Name="Source[1].propertiesCount" Type="Int">11</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="Source[2].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[2].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[2].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[2].itemID" Type="Ref">/Poste de travail/SubVIs</Property>
				<Property Name="Source[2].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[2].type" Type="Str">Container</Property>
				<Property Name="Source[3].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[3].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[3].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[3].itemID" Type="Ref">/Poste de travail/Type Def</Property>
				<Property Name="Source[3].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[3].type" Type="Str">Container</Property>
				<Property Name="Source[4].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[4].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[4].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[4].itemID" Type="Ref">/Poste de travail/Icons</Property>
				<Property Name="Source[4].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[4].type" Type="Str">Container</Property>
				<Property Name="Source[5].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[5].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[5].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[5].itemID" Type="Ref">/Poste de travail/dll</Property>
				<Property Name="Source[5].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[5].type" Type="Str">Container</Property>
				<Property Name="Source[6].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[6].Container.depDestIndex" Type="Int">0</Property>
				<Property Name="Source[6].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[6].itemID" Type="Ref">/Poste de travail/Config</Property>
				<Property Name="Source[6].sourceInclusion" Type="Str">Include</Property>
				<Property Name="Source[6].type" Type="Str">Container</Property>
				<Property Name="SourceCount" Type="Int">7</Property>
				<Property Name="TgtF_companyName" Type="Str">THALES LAS FRANCE</Property>
				<Property Name="TgtF_fileDescription" Type="Str">New Focus</Property>
				<Property Name="TgtF_internalName" Type="Str">New Focus</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2022 THALES LAS FRANCE</Property>
				<Property Name="TgtF_productName" Type="Str">New Focus</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{1BEEA345-0B10-49C2-96E9-8FE5FC43D90C}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">New Focus.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
		</Item>
	</Item>
</Project>
