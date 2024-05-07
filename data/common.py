class GameKindEnum:
    GameKindSlotGame = 1  # 老虎機
    GameKindSpeciualGame = 2  # 特色遊戲
    GameKindMMO = 3  # 多人


class GameStateEnum:
    GameStateOpen = 1
    GameStateMaintain = 2
    GameStateClosed = 3
    GameStateHidden = 4


class ItemTypeEnum:
    ItemTypeGameCoin = 1  # 遊戲幣
    ItemTypeDiamond = 2  # 鑽石


class LobbyStateEnum:
    LobbyStateOpen = 1
    LobbyStateMaintain = 2
    LobbyStateClosed = 3
    LobbyStateHidden = 4


class LobbyType:
    LobbyTypeArcade = 1  # 電子館
    LobbyTypeOther = 2  # 其他


class MailGroupTypeEnum:
    MailGroupTypeReceive = 1  # 領取
    MailGroupTypeMail = 2  # 信件
    MailGroupTypeMailGift = 3  # 收禮


class OpCode:
    S2CKick = 1  # 剔除玩家 只走error 流程
    S2CLogin = 2  # 玩家登入
    S2CSlotGameFlow = 3  # Slot流程
    C2SSlotGameFlow = 4  # Slot流程
    S2CMMOGameFlow = 5  # MMO流程
    C2SMMOGameFlow = 6  # MMO流程
    C2SSlotTableFlow = 7  # Slot桌流程
    C2SSlotTableFlow = 8  # Slot桌流程
    S2CChat = 9  # 聊天室
    C2SPing = 10  # ping
    S2CPong = 11  # pong
    C2SSystemFlow = 12  # 系統流程
    S2CSystemFlow = 13  # 系統流程
    C2SPlayerFlow = 14  # 玩家流程
    S2CPlayerFlow = 15  # 玩家流程
    C2SSpecialGameFlow = 16  # 特殊遊戲流程
    S2CSpecialGameFlow = 17  # 特殊遊戲流程
    C2SJackpotFlow = 18  # Jackpot流程
    S2CJackpotFlow = 19  # Jackpot流程
    C2SActivityFlow = 20  # 活動流程
    S2CActivityFlow = 21  # 活動流程
    S2CGetMail = 22  # 收到信


class PlayerAuthTypeEnum:
    PlayerAuthAnonymously = 1  # 立即玩
    PlayerAuthAccount = 2  # 一般帳號
    PlayerAuthGoogle = 3
    PlayerAuthApple = 4
    PlayerAuthFB = 5
    PlayerAuthLine = 6


class PlayerChangeNameEnum:
    PlayerNotCasual = 1  # 未完成首儲或綁定手機號碼
    PlayerCanChangeName = 2  # 可以改名
    PlayerAlreadyChangeName = 3  # 已改名


class PlayerGameCoinLogTypeEnum:
    PlayerGameCoinLogTypeSystemAdd = 1  # 系統加幣
    PlayerGameCoinLogTypeSystemSub = 2  # 系統扣幣
    PlayerGameCoinLogTypeActivity = 3  # 活動回饋


class PlayerPermission:
    PlayerPermissionLevelUp = 1  # 升等權限
    PlayerPermissionHappyNewYear2024Activity = 2  # 2024過年活動權限


class PlayerTypeEnum:
    PlayerTypeCasual = 1  # 非正式會員
    PlayerTypeRegular = 2  # 正式會員 綁定手機或首購才能轉換正式會員
