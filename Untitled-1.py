<?xml version="1.0" encoding="utf-8"?>
<Project ToolsVersion="15.0" DefaultTargets="Build" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <Import Project="..\packages\Microsoft.CodeDom.Providers.DotNetCompilerPlatform.2.0.0\build\net46\Microsoft.CodeDom.Providers.DotNetCompilerPlatform.props" Condition="Exists('..\packages\Microsoft.CodeDom.Providers.DotNetCompilerPlatform.2.0.0\build\net46\Microsoft.CodeDom.Providers.DotNetCompilerPlatform.props')" />
  <Import Project="$(MSBuildExtensionsPath)\$(MSBuildToolsVersion)\Microsoft.Common.props" Condition="Exists('$(MSBuildExtensionsPath)\$(MSBuildToolsVersion)\Microsoft.Common.props')" />
  <PropertyGroup>
    <Configuration Condition=" '$(Configuration)' == '' ">Debug</Configuration>
    <Platform Condition=" '$(Platform)' == '' ">AnyCPU</Platform>
    <ProductVersion>
    </ProductVersion>
    <SchemaVersion>2.0</SchemaVersion>
    <ProjectGuid>{B9D73497-7909-4261-A2C5-52991A108602}</ProjectGuid>
    <ProjectTypeGuids>{349c5851-65df-11da-9384-00065b846f21};{fae04ec0-301f-11d3-bf4b-00c04f79efbc}</ProjectTypeGuids>
    <OutputType>Library</OutputType>
    <AppDesignerFolder>Properties</AppDesignerFolder>
    <RootNamespace>Vidly</RootNamespace>
    <AssemblyName>Vidly</AssemblyName>
    <TargetFrameworkVersion>v4.6.1</TargetFrameworkVersion>
    <MvcBuildViews>false</MvcBuildViews>
    <UseIISExpress>true</UseIISExpress>
    <Use64BitIISExpress />
    <IISExpressSSLPort />
    <IISExpressAnonymousAuthentication />
    <IISExpressWindowsAuthentication />
    <IISExpressUseClassicPipelineMode />
    <UseGlobalApplicationHostFile />
    <NuGetPackageImportStamp>
    </NuGetPackageImportStamp>
  </PropertyGroup>
  <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|AnyCPU' ">
    <DebugSymbols>true</DebugSymbols>
    <DebugType>full</DebugType>
    <Optimize>false</Optimize>
    <OutputPath>bin\</OutputPath>
    <DefineConstants>DEBUG;TRACE</DefineConstants>
    <ErrorReport>prompt</ErrorReport>
    <WarningLevel>4</WarningLevel>
  </PropertyGroup>
  <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Release|AnyCPU' ">
    <DebugSymbols>true</DebugSymbols>
    <DebugType>pdbonly</DebugType>
    <Optimize>true</Optimize>
    <OutputPath>bin\</OutputPath>
    <DefineConstants>TRACE</DefineConstants>
    <ErrorReport>prompt</ErrorReport>
    <WarningLevel>4</WarningLevel>
  </PropertyGroup>
  <ItemGroup>
    <Reference Include="Microsoft.CSharp" />
    <Reference Include="System" />
    <Reference Include="System.Data" />
    <Reference Include="System.Drawing" />
    <Reference Include="System.Web.DynamicData" />
    <Reference Include="System.Web.Entity" />
    <Reference Include="System.Web.ApplicationServices" />
    <Reference Include="System.ComponentModel.DataAnnotations" />
    <Reference Include="System.Core" />
    <Reference Include="System.Data.DataSetExtensions" />
    <Reference Include="System.Xml.Linq" />
    <Reference Include="System.Web" />
    <Reference Include="System.Web.Extensions" />
    <Reference Include="System.Web.Abstractions" />
    <Reference Include="System.Web.Routing" />
    <Reference Include="System.Xml" />
    <Reference Include="System.Configuration" />
    <Reference Include="System.Web.Services" />
    <Reference Include="System.EnterpriseServices" />
    <Reference Include="Microsoft.Web.Infrastructure, Version=1.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, processorArchitecture=MSIL">
      <Private>True</Private>
      <HintPath>..\packages\Microsoft.Web.Infrastructure.1.0.0.0\lib\net40\Microsoft.Web.Infrastructure.dll</HintPath>
    </Reference>
    <Reference Include="System.Net.Http">
    </Reference>
    <Reference Include="System.Net.Http.WebRequest">
    </Reference>
    <Reference Include="System.Web.Helpers, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, processorArchitecture=MSIL">
      <Private>True</Private>
      <HintPath>..\packages\Microsoft.AspNet.WebPages.3.2.4\lib\net45\System.Web.Helpers.dll</HintPath>
    </Reference>
    <Reference Include="System.Web.Mvc, Version=5.2.4.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, processorArchitecture=MSIL">
      <Private>True</Private>
      <HintPath>..\packages\Microsoft.AspNet.Mvc.5.2.4\lib\net45\System.Web.Mvc.dll</HintPath>
    </Reference>
    <Reference Include="System.Web.Optimization">
      <HintPath>..\packages\Microsoft.AspNet.Web.Optimization.1.1.3\lib\net40\System.Web.Optimization.dll</HintPath>
    </Reference>
    <Reference Include="System.Web.Razor, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, processorArchitecture=MSIL">
      <Private>True</Private>
      <HintPath>..\packages\Microsoft.AspNet.Razor.3.2.4\lib\net45\System.Web.Razor.dll</HintPath>
    </Reference>
    <Reference Include="System.Web.WebPages, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, processorArchitecture=MSIL">
      <Private>True</Private>
      <HintPath>..\packages\Microsoft.AspNet.WebPages.3.2.4\lib\net45\System.Web.WebPages.dll</HintPath>
    </Reference>
    <Reference Include="System.Web.WebPages.Deployment, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, processorArchitecture=MSIL">
      <Private>True</Private>
      <HintPath>..\packages\Microsoft.AspNet.WebPages.3.2.4\lib\net45\System.Web.WebPages.Deployment.dll</HintPath>
    </Reference>
    <Reference Include="System.Web.WebPages.Razor, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, processorArchitecture=MSIL">
      <Private>True</Private>
      <HintPath>..\packages\Microsoft.AspNet.WebPages.3.2.4\lib\net45\System.Web.WebPages.Razor.dll</HintPath>
    </Reference>
    <Reference Include="Newtonsoft.Json">
      <HintPath>..\packages\Newtonsoft.Json.11.0.1\lib\net45\Newtonsoft.Json.dll</HintPath>
    </Reference>
    <Reference Include="WebGrease">
      <Private>True</Private>
      <HintPath>..\packages\WebGrease.1.6.0\lib\WebGrease.dll</HintPath>
    </Reference>
    <Reference Include="Antlr3.Runtime">
      <Private>True</Private>
      <HintPath>..\packages\Antlr.3.5.0.2\lib\Antlr3.Runtime.dll</HintPath>
    </Reference>
  </ItemGroup>
  <ItemGroup>
    <Reference Include="EntityFramework">
      <HintPath>..\packages\EntityFramework.6.2.0\lib\net45\EntityFramework.dll</HintPath>
    </Reference>
    <Reference Include="EntityFramework.SqlServer">
      <HintPath>..\packages\EntityFramework.6.2.0\lib\net45\EntityFramework.SqlServer.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.AspNet.Identity.Core">
      <HintPath>..\packages\Microsoft.AspNet.Identity.Core.2.2.2\lib\net45\Microsoft.AspNet.Identity.Core.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.AspNet.Identity.Owin">
      <HintPath>..\packages\Microsoft.AspNet.Identity.Owin.2.2.2\lib\net45\Microsoft.AspNet.Identity.Owin.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.AspNet.Identity.EntityFramework">
      <HintPath>..\packages\Microsoft.AspNet.Identity.EntityFramework.2.2.2\lib\net45\Microsoft.AspNet.Identity.EntityFramework.dll</HintPath>
    </Reference>
    <Reference Include="Owin">
      <HintPath>..\packages\Owin.1.0\lib\net40\Owin.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.Owin">
      <HintPath>..\packages\Microsoft.Owin.4.0.0\lib\net451\Microsoft.Owin.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.Owin.Host.SystemWeb">
      <HintPath>..\packages\Microsoft.Owin.Host.SystemWeb.4.0.0\lib\net451\Microsoft.Owin.Host.SystemWeb.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.Owin.Security">
      <HintPath>..\packages\Microsoft.Owin.Security.4.0.0\lib\net451\Microsoft.Owin.Security.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.Owin.Security.Cookies">
      <HintPath>..\packages\Microsoft.Owin.Security.Facebook.4.0.0\lib\net451\Microsoft.Owin.Security.Facebook.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.Owin.Security.Cookies">
      <HintPath>..\packages\Microsoft.Owin.Security.Cookies.4.0.0\lib\net451\Microsoft.Owin.Security.Cookies.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.Owin.Security.Google">
      <HintPath>..\packages\Microsoft.Owin.Security.Google.4.0.0\lib\net451\Microsoft.Owin.Security.Google.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.Owin.Security.Twitter">
      <HintPath>..\packages\Microsoft.Owin.Security.Twitter.4.0.0\lib\net451\Microsoft.Owin.Security.Twitter.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.Owin.Security.MicrosoftAccount">
      <HintPath>..\packages\Microsoft.Owin.Security.MicrosoftAccount.4.0.0\lib\net451\Microsoft.Owin.Security.MicrosoftAccount.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.Owin.Security.OAuth">
      <HintPath>..\packages\Microsoft.Owin.Security.OAuth.4.0.0\lib\net451\Microsoft.Owin.Security.OAuth.dll</HintPath>
    </Reference>
    <Reference Include="System.Diagnostics.DiagnosticSource">
      <HintPath>..\packages\System.Diagnostics.DiagnosticSource.4.4.1\lib\net46\System.Diagnostics.DiagnosticSource.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.AspNet.TelemetryCorrelation">
      <HintPath>..\packages\Microsoft.AspNet.TelemetryCorrelation.1.0.0\lib\net45\Microsoft.AspNet.TelemetryCorrelation.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.ApplicationInsights">
      <HintPath>..\packages\Microsoft.ApplicationInsights.2.5.1\lib\net46\Microsoft.ApplicationInsights.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.AI.Agent.Intercept">
      <HintPath>..\packages\Microsoft.ApplicationInsights.Agent.Intercept.2.4.0\lib\net45\Microsoft.AI.Agent.Intercept.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.AI.DependencyCollector">
      <HintPath>..\packages\Microsoft.ApplicationInsights.DependencyCollector.2.5.1\lib\net45\Microsoft.AI.DependencyCollector.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.AI.PerfCounterCollector">
      <HintPath>..\packages\Microsoft.ApplicationInsights.PerfCounterCollector.2.5.1\lib\net45\Microsoft.AI.PerfCounterCollector.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.AI.ServerTelemetryChannel">
      <HintPath>..\packages\Microsoft.ApplicationInsights.WindowsServer.TelemetryChannel.2.5.1\lib\net45\Microsoft.AI.ServerTelemetryChannel.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.AI.WindowsServer">
      <HintPath>..\packages\Microsoft.ApplicationInsights.WindowsServer.2.5.1\lib\net45\Microsoft.AI.WindowsServer.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.AI.Web">
      <HintPath>..\packages\Microsoft.ApplicationInsights.Web.2.5.1\lib\net45\Microsoft.AI.Web.dll</HintPath>
    </Reference>
    <Reference Include="Microsoft.CodeDom.Providers.DotNetCompilerPlatform">
      <HintPath>..\packages\Microsoft.CodeDom.Providers.DotNetCompilerPlatform.2.0.0\lib\net45\Microsoft.CodeDom.Providers.DotNetCompilerPlatform.dll</HintPath>
    </Reference>
  </ItemGroup>
  <ItemGroup>
    <Compile Include="App_Start\BundleConfig.cs" />
    <Compile Include="App_Start\FilterConfig.cs" />
    <Compile Include="App_Start\IdentityConfig.cs" />
    <Compile Include="App_Start\RouteConfig.cs" />
    <Compile Include="App_Start\Startup.Auth.cs" />
    <Compile Include="Controllers\AccountController.cs" />
    <Compile Include="Controllers\CustomerController.cs" />
    <Compile Include="Controllers\HomeController.cs" />
    <Compile Include="Controllers\ManageController.cs" />
    <Compile Include="Controllers\MoviesController.cs" />
    <Compile Include="Global.asax.cs">
      <DependentUpon>Global.asax</DependentUpon>
    </Compile>
    <Compile Include="Models\AccountViewModels.cs" />
    <Compile Include="Models\Customer.cs" />
    <Compile Include="Models\IdentityModels.cs" />
    <Compile Include="Models\ManageViewModels.cs" />
    <Compile Include="Models\Movie.cs" />
    <Compile Include="Properties\AssemblyInfo.cs" />
    <Compile Include="Startup.cs" />
    <Compile Include="ViewModels\RandomMovieViewModel.cs" />
  </ItemGroup>
  <ItemGroup>
    <Content Include="Content\bootstrap-lumen.css" />
    <Content Include="Content\bootstrap-theme.css" />
    <Content Include="Content\bootstrap-theme.min.css" />
    <Content Include="Content\bootstrap.css" />
    <Content Include="Content\bootstrap.min.css" />
    <Content Include="favicon.ico" />
    <Content Include="fonts\glyphicons-halflings-regular.svg" />
    <Content Include="Global.asax" />
    <Content Include="Content\Site.css" />
    <Content Include="Scripts\bootstrap.js" />
    <Content Include="Scripts\bootstrap.min.js" />
    <Content Include="ApplicationInsights.config">
      <CopyToOutputDirectory>PreserveNewest</CopyToOutputDirectory>
    </Content>
    <None Include="Scripts\jquery-3.3.1.intellisense.js" />
    <Content Include="Scripts\jquery-3.3.1.js" />
    <Content Include="Scripts\jquery-3.3.1.min.js" />
    <Content Include="Scripts\jquery-3.3.1.slim.js" />
    <Content Include="Scripts\jquery-3.3.1.slim.min.js" />
    <None Include="Scripts\jquery.validate-vsdoc.js" />
    <Content Include="Scripts\jquery.validate.js" />
    <Content Include="Scripts\jquery.validate.min.js" />
    <Content Include="Scripts\jquery.validate.unobtrusive.js" />
    <Content Include="Scripts\jquery.validate.unobtrusive.min.js" />
    <Content Include="Scripts\modernizr-2.8.3.js" />
    <Content Include="Web.config" />
    <Content Include="Web.Debug.config">
      <DependentUpon>Web.config</DependentUpon>
    </Content>
    <Content Include="Web.Release.config">
      <DependentUpon>Web.config</DependentUpon>
    </Content>
    <Content Include="Views\Web.config" />
    <Content Include="Views\_ViewStart.cshtml" />
    <Content Include="Views\Shared\Error.cshtml" />
    <Content Include="Views\Shared\_Layout.cshtml" />
    <Content Include="Views\Home\About.cshtml" />
    <Content Include="Views\Home\Contact.cshtml" />
    <Content Include="Views\Home\Index.cshtml" />
    <Content Include="Views\Account\_ExternalLoginsListPartial.cshtml" />
    <Content Include="Views\Account\ConfirmEmail.cshtml" />
    <Content Include="Views\Account\ExternalLoginConfirmation.cshtml" />
    <Content Include="Views\Account\ExternalLoginFailure.cshtml" />
    <Content Include="Views\Account\ForgotPassword.cshtml" />
    <Content Include="Views\Account\ForgotPasswordConfirmation.cshtml" />
    <Content Include="Views\Account\Login.cshtml" />
    <Content Include="Views\Account\Register.cshtml" />
    <Content Include="Views\Account\ResetPassword.cshtml" />
    <Content Include="Views\Account\ResetPasswordConfirmation.cshtml" />
    <Content Include="Views\Account\SendCode.cshtml" />
    <Content Include="Views\Account\VerifyCode.cshtml" />
    <Content Include="Views\Manage\AddPhoneNumber.cshtml" />
    <Content Include="Views\Manage\ChangePassword.cshtml" />
    <Content Include="Views\Manage\Index.cshtml" />
    <Content Include="Views\Manage\ManageLogins.cshtml" />
    <Content Include="Views\Manage\SetPassword.cshtml" />
    <Content Include="Views\Manage\VerifyPhoneNumber.cshtml" />
    <Content Include="Views\Shared\Lockout.cshtml" />
    <Content Include="Views\Shared\_LoginPartial.cshtml" />
    <Content Include="Views\Movies\Random.cshtml" />
    <Content Include="Views\Shared\_NavBar.cshtml" />
    <Content Include="Views\Movies\Customers.cshtml" />
  </ItemGroup>
  <ItemGroup>
    <Folder Include="App_Data\" />
    <Folder Include="Views\Customer\" />
  </ItemGroup>
  <ItemGroup>
    <Content Include="fonts\glyphicons-halflings-regular.woff2" />
    <Content Include="fonts\glyphicons-halflings-regular.woff" />
    <Content Include="fonts\glyphicons-halflings-regular.ttf" />
    <Content Include="fonts\glyphicons-halflings-regular.eot" />
    <Content Include="Content\bootstrap.min.css.map" />
    <Content Include="Content\bootstrap.css.map" />
    <Content Include="Content\bootstrap-theme.min.css.map" />
    <Content Include="Content\bootstrap-theme.css.map" />
    <None Include="packages.config" />
    <Content Include="Scripts\jquery-3.3.1.slim.min.map" />
    <Content Include="Scripts\jquery-3.3.1.min.map" />
  </ItemGroup>
  <PropertyGroup>
    <VisualStudioVersion Condition="'$(VisualStudioVersion)' == ''">10.0</VisualStudioVersion>
    <VSToolsPath Condition="'$(VSToolsPath)' == ''">$(MSBuildExtensionsPath32)\Microsoft\VisualStudio\v$(VisualStudioVersion)</VSToolsPath>
  </PropertyGroup>
  <Import Project="$(MSBuildBinPath)\Microsoft.CSharp.targets" />
  <Import Project="$(VSToolsPath)\WebApplications\Microsoft.WebApplication.targets" Condition="'$(VSToolsPath)' != ''" />
  <Import Project="$(MSBuildExtensionsPath32)\Microsoft\VisualStudio\v10.0\WebApplications\Microsoft.WebApplication.targets" Condition="false" />
  <Target Name="MvcBuildViews" AfterTargets="AfterBuild" Condition="'$(MvcBuildViews)'=='true'">
    <AspNetCompiler VirtualPath="temp" PhysicalPath="$(WebProjectOutputDir)" />
  </Target>
  <ProjectExtensions>
    <VisualStudio>
      <FlavorProperties GUID="{349c5851-65df-11da-9384-00065b846f21}">
        <WebProjectProperties>
          <UseIIS>True</UseIIS>
          <AutoAssignPort>True</AutoAssignPort>
          <DevelopmentServerPort>54798</DevelopmentServerPort>
          <DevelopmentServerVPath>/</DevelopmentServerVPath>
          <IISUrl>http://localhost:54798/</IISUrl>
          <NTLMAuthentication>False</NTLMAuthentication>
          <UseCustomServer>False</UseCustomServer>
          <CustomServerUrl>
          </CustomServerUrl>
          <SaveServerSettingsInUserFile>False</SaveServerSettingsInUserFile>
        </WebProjectProperties>
      </FlavorProperties>
    </VisualStudio>
  </ProjectExtensions>
  <Target Name="EnsureNuGetPackageBuildImports" BeforeTargets="PrepareForBuild">
    <PropertyGroup>
      <ErrorText>This project references NuGet package(s) that are missing on this computer. Use NuGet Package Restore to download them.  For more information, see http://go.microsoft.com/fwlink/?LinkID=322105. The missing file is {0}.</ErrorText>
    </PropertyGroup>
    <Error Condition="!Exists('..\packages\Microsoft.CodeDom.Providers.DotNetCompilerPlatform.2.0.0\build\net46\Microsoft.CodeDom.Providers.DotNetCompilerPlatform.props')" Text="$([System.String]::Format('$(ErrorText)', '..\packages\Microsoft.CodeDom.Providers.DotNetCompilerPlatform.2.0.0\build\net46\Microsoft.CodeDom.Providers.DotNetCompilerPlatform.props'))" />
  </Target>
  <!-- To modify your build process, add your task inside one of the targets below and uncomment it.
       Other similar extension points exist, see Microsoft.Common.targets.
  <Target Name="BeforeBuild">
  </Target>
  <Target Name="AfterBuild">
  </Target> -->
</Project>